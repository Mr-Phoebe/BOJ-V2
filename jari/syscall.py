# basic syscall table
# 0 for prohibited
# 1 for permitted
# 2 for extended usage
SYSCALL = (
    ( 0, 'restart_syscall', ),
    ( 1, 'exit', ),
    ( 0, 'fork', ),
    ( 1, 'read', ),
    ( 1, 'write', ),
    ( 1, 'open', ),
    ( 1, 'close', ),
    ( 0, 'waitpid', ),
    ( 0, 'creat', ),
    ( 0, 'link', ),
    ( 1, 'unlink', ),
    ( 1, 'execve', ),
    ( 0, 'chdir', ),
    ( 1, 'time', ),
    ( 0, 'mknod', ),
    ( 0, 'chmod', ),
    ( 0, 'lchown', ),
    ( 0, 'break', ),
    ( 0, 'oldstat', ),
    ( 0, 'lseek', ),
    ( 0, 'getpid', ),
    ( 0, 'mount', ),
    ( 0, 'umount', ),
    ( 0, 'setuid', ),
    ( 0, 'getuid', ),
    ( 0, 'stime', ),
    ( 0, 'ptrace', ),
    ( 0, 'alarm', ),
    ( 0, 'oldfstat', ),
    ( 0, 'pause', ),
    ( 0, 'utime', ),
    ( 0, 'stty', ),
    ( 0, 'gtty', ),
    ( 1, 'access', ),
    ( 0, 'nice', ),
    ( 0, 'ftime', ),
    ( 0, 'sync', ),
    ( 0, 'kill', ),
    ( 0, 'rename', ),
    ( 0, 'mkdir', ),
    ( 0, 'rmdir', ),
    ( 0, 'dup', ),
    ( 0, 'pipe', ),
    ( 1, 'times', ),
    ( 0, 'prof', ),
    ( 2, 'brk', ),
    ( 0, 'setgid', ),
    ( 0, 'getgid', ),
    ( 0, 'signal', ),
    ( 0, 'geteuid', ),
    ( 0, 'getegid', ),
    ( 0, 'acct', ),
    ( 0, 'umount2', ),
    ( 0, 'lock', ),
    ( 0, 'ioctl', ),
    ( 0, 'fcntl', ),
    ( 0, 'mpx', ),
    ( 0, 'setpgid', ),
    ( 0, 'ulimit', ),
    ( 0, 'oldolduname', ),
    ( 0, 'umask', ),
    ( 0, 'chroot', ),
    ( 0, 'ustat', ),
    ( 0, 'dup2', ),
    ( 0, 'getppid', ),
    ( 0, 'getpgrp', ),
    ( 0, 'setsid', ),
    ( 0, 'sigaction', ),
    ( 0, 'sgetmask', ),
    ( 0, 'ssetmask', ),
    ( 0, 'setreuid', ),
    ( 0, 'setregid', ),
    ( 0, 'sigsuspend', ),
    ( 0, 'sigpending', ),
    ( 0, 'sethostname', ),
    ( 0, 'setrlimit', ),
    ( 0, 'getrlimit', ),
    ( 0, 'getrusage', ),
    ( 0, 'gettimeofday', ),
    ( 0, 'settimeofday', ),
    ( 0, 'getgroups', ),
    ( 0, 'setgroups', ),
    ( 0, 'select', ),
    ( 0, 'symlink', ),
    ( 0, 'oldlstat', ),
    ( 1, 'readlink', ),
    ( 0, 'uselib', ),
    ( 0, 'swapon', ),
    ( 0, 'reboot', ),
    ( 0, 'readdir', ),
    ( 2, 'mmap', ),
    ( 2, 'munmap', ),
    ( 0, 'truncate', ),
    ( 0, 'ftruncate', ),
    ( 0, 'fchmod', ),
    ( 0, 'fchown', ),
    ( 0, 'getpriority', ),
    ( 0, 'setpriority', ),
    ( 0, 'profil', ),
    ( 0, 'statfs', ),
    ( 0, 'fstatfs', ),
    ( 0, 'ioperm', ),
    ( 0, 'socketcall', ),
    ( 0, 'syslog', ),
    ( 0, 'setitimer', ),
    ( 0, 'getitimer', ),
    ( 0, 'stat', ),
    ( 0, 'lstat', ),
    ( 0, 'fstat', ),
    ( 0, 'olduname', ),
    ( 0, 'iopl', ),
    ( 0, 'vhangup', ),
    ( 0, 'idle', ),
    ( 0, 'vm86old', ),
    ( 0, 'wait4', ),
    ( 0, 'swapoff', ),
    ( 0, 'sysinfo', ),
    ( 0, 'ipc', ),
    ( 0, 'fsync', ),
    ( 0, 'sigreturn', ),
    ( 0, 'clone', ),
    ( 0, 'setdomainname', ),
    ( 1, 'uname', ),
    ( 0, 'modify_ldt', ),
    ( 0, 'adjtimex', ),
    ( 2, 'mprotect', ),
    ( 0, 'sigprocmask', ),
    ( 0, 'create_module', ),
    ( 0, 'init_module', ),
    ( 0, 'delete_module', ),
    ( 0, 'get_kernel_syms', ),
    ( 0, 'quotactl', ),
    ( 0, 'getpgid', ),
    ( 0, 'fchdir', ),
    ( 0, 'bdflush', ),
    ( 0, 'sysfs', ),
    ( 0, 'personality', ),
    ( 0, 'afs_syscall', ),
    ( 0, 'setfsuid', ),
    ( 0, 'setfsgid', ),
    ( 1, '_llseek', ),
    ( 0, 'getdents', ),
    ( 0, '_newselect', ),
    ( 0, 'flock', ),
    ( 0, 'msync', ),
    ( 0, 'readv', ),
    ( 1, 'writev', ),
    ( 0, 'getsid', ),
    ( 0, 'fdatasync', ),
    ( 0, '_sysctl', ),
    ( 0, 'mlock', ),
    ( 0, 'munlock', ),
    ( 0, 'mlockall', ),
    ( 0, 'munlockall', ),
    ( 0, 'sched_setparam', ),
    ( 0, 'sched_getparam', ),
    ( 0, 'sched_setscheduler', ),
    ( 0, 'sched_getscheduler', ),
    ( 0, 'sched_yield', ),
    ( 0, 'sched_get_priority_max', ),
    ( 0, 'sched_get_priority_min', ),
    ( 0, 'sched_rr_get_interval', ),
    ( 0, 'nanosleep', ),
    ( 0, 'mremap', ),
    ( 0, 'setresuid', ),
    ( 0, 'getresuid', ),
    ( 0, 'vm86', ),
    ( 0, 'query_module', ),
    ( 0, 'poll', ),
    ( 0, 'nfsservctl', ),
    ( 0, 'setresgid', ),
    ( 0, 'getresgid', ),
    ( 0, 'prctl', ),
    ( 0, 'rt_sigreturn', ),
    ( 1, 'rt_sigaction', ),
    ( 1, 'rt_sigprocmask', ),
    ( 0, 'rt_sigpending', ),
    ( 0, 'rt_sigtimedwait', ),
    ( 0, 'rt_sigqueueinfo', ),
    ( 0, 'rt_sigsuspend', ),
    ( 0, 'pread64', ),
    ( 0, 'pwrite64', ),
    ( 0, 'chown', ),
    ( 0, 'getcwd', ),
    ( 0, 'capget', ),
    ( 0, 'capset', ),
    ( 0, 'sigaltstack', ),
    ( 0, 'sendfile', ),
    ( 0, 'getpmsg', ),
    ( 0, 'putpmsg', ),
    ( 0, 'vfork', ),
    ( 1, 'ugetrlimit', ),
    ( 2, 'mmap2', ),
    ( 0, 'truncate64', ),
    ( 0, 'ftruncate64', ),
    ( 1, 'stat64', ),
    ( 0, 'lstat64', ),
    ( 1, 'fstat64', ),
    ( 0, 'lchown32', ),
    ( 1, 'getuid32', ),
    ( 1, 'getgid32', ),
    ( 1, 'geteuid32', ),
    ( 1, 'getegid32', ),
    ( 0, 'setreuid32', ),
    ( 0, 'setregid32', ),
    ( 0, 'getgroups32', ),
    ( 0, 'setgroups32', ),
    ( 0, 'fchown32', ),
    ( 0, 'setresuid32', ),
    ( 0, 'getresuid32', ),
    ( 0, 'setresgid32', ),
    ( 0, 'getresgid32', ),
    ( 0, 'chown32', ),
    ( 0, 'setuid32', ),
    ( 0, 'setgid32', ),
    ( 0, 'setfsuid32', ),
    ( 0, 'setfsgid32', ),
    ( 0, 'pivot_root', ),
    ( 0, 'mincore', ),
    ( 0, 'madvise', ),
    ( 0, 'getdents64', ),
    ( 0, 'fcntl64', ),
    ( 0, 'gettid', ),
    ( 0, 'readahead', ),
    ( 0, 'setxattr', ),
    ( 0, 'lsetxattr', ),
    ( 0, 'fsetxattr', ),
    ( 0, 'getxattr', ),
    ( 0, 'lgetxattr', ),
    ( 0, 'fgetxattr', ),
    ( 0, 'listxattr', ),
    ( 0, 'llistxattr', ),
    ( 0, 'flistxattr', ),
    ( 0, 'removexattr', ),
    ( 0, 'lremovexattr', ),
    ( 0, 'fremovexattr', ),
    ( 0, 'tkill', ),
    ( 0, 'sendfile64', ),
    ( 0, 'futex', ),
    ( 0, 'sched_setaffinity', ),
    ( 1, 'sched_getaffinity', ),
    ( 0, 'set_thread_area', ),
    ( 0, 'get_thread_area', ),
    ( 2, 'io_setup', ),
    ( 0, 'io_destroy', ),
    ( 0, 'io_getevents', ),
    ( 0, 'io_submit', ),
    ( 0, 'io_cancel', ),
    ( 0, 'fadvise64', ),
    ( 0, '(null)', ),
    ( 0, 'exit_group', ),
    ( 0, 'lookup_dcookie', ),
    ( 1, 'epoll_create', ),
    ( 0, 'epoll_ctl', ),
    ( 0, 'epoll_wait', ),
    ( 0, 'remap_file_pages', ),
    ( 0, 'set_tid_address', ),
    ( 0, 'timer_create', ),
    ( 1, 'timer_settime', ),
    ( 0, 'timer_gettime', ),
    ( 0, 'timer_getoverrun', ),
    ( 0, 'timer_delete', ),
    ( 0, 'clock_settime', ),
    ( 0, 'clock_gettime', ),
    ( 0, 'clock_getres', ),
    ( 0, 'clock_nanosleep', ),
    ( 0, 'statfs64', ),
    ( 0, 'fstatfs64', ),
    ( 0, 'tgkill', ),
    ( 0, 'utimes', ),
    ( 1, 'fadvise64_64', ),
    ( 0, 'vserver', ),
    ( 0, 'mbind', ),
    ( 0, 'get_mempolicy', ),
    ( 0, 'set_mempolicy', ),
    ( 0, 'mq_open', ),
    ( 0, 'mq_unlink', ),
    ( 0, 'mq_timedsend', ),
    ( 0, 'mq_timedreceive', ),
    ( 0, 'mq_notify', ),
    ( 0, 'mq_getsetattr', ),
    ( 0, 'kexec_load', ),
    ( 0, 'waitid', ),
    ( 0, '(null)', ),
    ( 0, 'add_key', ),
    ( 0, 'request_key', ),
    ( 0, 'keyctl', ),
    ( 0, 'ioprio_set', ),
    ( 0, 'ioprio_get', ),
    ( 0, 'inotify_init', ),
    ( 0, 'inotify_add_watch', ),
    ( 0, 'inotify_rm_watch', ),
    ( 0, 'migrate_pages', ),
    ( 0, 'openat', ),
    ( 0, 'mkdirat', ),
    ( 0, 'mknodat', ),
    ( 0, 'fchownat', ),
    ( 0, 'futimesat', ),
    ( 0, 'fstatat64', ),
    ( 0, 'unlinkat', ),
    ( 0, 'renameat', ),
    ( 0, 'linkat', ),
    ( 0, 'symlinkat', ),
    ( 0, 'readlinkat', ),
    ( 0, 'fchmodat', ),
    ( 0, 'faccessat', ),
    ( 0, 'pselect6', ),
    ( 0, 'ppoll', ),
    ( 0, 'unshare', ),
    ( 0, 'set_robust_list', ),
    ( 0, 'get_robust_list', ),
    ( 1, 'splice', ),
    ( 0, 'sync_file_range', ),
    ( 0, 'tee', ),
    ( 0, 'vmsplice', ),
    ( 0, 'move_pages', ),
    ( 0, 'getcpu', ),
    ( 0, 'epoll_pwait', ),
    ( 0, 'utimensat', ),
    ( 0, 'signalfd', ),
    ( 0, 'timerfd_create', ),
    ( 0, 'eventfd', ),
    ( 0, 'fallocate', ),
    ( 0, 'timerfd_settime', ),
    ( 0, 'timerfd_gettime', ),
    ( 0, 'signalfd4', ),
    ( 0, 'eventfd2', ),
    ( 0, 'epoll_create1', ),
    ( 0, 'dup3', ),
    ( 0, 'pipe2', ),
    ( 0, 'inotify_init1', ),
    ( 0, 'preadv', ),
    ( 0, 'pwritev', ),
    ( 0, 'rt_tgsigqueueinfo', ),
    ( 0, 'perf_counter_open', ),
)

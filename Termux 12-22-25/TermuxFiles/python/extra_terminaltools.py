""" Marcellus Murray            2025            TerminalTools
"""
HelpDictionary = {
    "bash --help": {
        "Version": {
            "GNU bash, version 5.2.26(1)-release-(x86_64-pc-msys)"
        },
        "Usage": { 
            "bash [GNU long option] [option] ...",
            "bash [GNU long option] [option] script-file ..."
        },
        "GNU long options": {
            "--debug",
            "--debugger",
            "--dump-po-strings",
            "--dump-strings",
            "--help",
            "--init-file",
            "--login",
            "--noediting",
            "--noprofile",
            "--norc",
            "--posix",
            "--pretty-print",
            "--protected",
            "--rcfile",
            "--restricted",
            "--verbose",
            "--version",
            "--wordexp"
        },
        "Shell options": {
            "-ilrsD or -c command or -O shopt_option         (invocation only)",
            "-abefhkmnptuvxBCEHPT or -o option"
        },
        "Directions": {
            "Type `bash -c \"help set\"' for more information about shell options.",
            "Type `bash -c help' for more information about shell builtin commands.",
            "Use the `bashbug' command to report bugs."
        },
        "Links": {
            "bash home page: <http://www.gnu.org/software/bash>",
            "General help using GNU software: <http://www.gnu.org/gethelp/>"    
        }
    },
    
    "bash -c \"help set\"" : {
        # [Set/Unset values] of (shell options)/(positional parameters).
        "set": "set [-abefhkmnptuvxBCEHPT] [-o option-name] [--] [-] [arg ...]",

        # Change the value of shell attributes and positional parameters, or
        # display the names and values of shell variables.
    
        "Options": {
            "-a  Mark variables which are modified or created for export.",
            "-b  Notify of job termination immediately.",
            "-e  Exit immediately if a command exits with a non-zero status.",
            "-f  Disable file name generation (globbing).",
            "-h  Remember the location of commands as they are looked up.",
            "-k  All assignment arguments are placed in the environment for a command, not just those that precede the command name.",
            "-m  Job control is enabled.",
            "-n  Read commands but do not execute them.",
            "-o option-name": {
                #Set the variable corresponding to option-name:
                "allexport": "same as -a",
                "braceexpand  same as -B",
                "emacs        use an emacs-style line editing interface",
                "errexit      same as -e",
                "errtrace     same as -E",
                "functrace    same as -T",
                "hashall      same as -h",
                "histexpand   same as -H",
                "history      enable command history",
                "igncr        on Cygwin, ignore \r in line endings",
                "ignoreeof    the shell will not exit upon reading EOF",
                "interactive-comments": "allow comments to appear in interactive commands",
                "        keyword      same as -k",
                "        monitor      same as -m",
                "        noclobber    same as -C",
                "        noexec       same as -n",
                "        noglob       same as -f",
                "        nolog        currently accepted but ignored",
                "        notify       same as -b",
                "        nounset      same as -u",
                "        onecmd       same as -t",
                "        physical     same as -P",
                "        pipefail     the return value of a pipeline is the status of",
          "                     the last command to exit with a non-zero status,",
          "                     or zero if no command exited with a non-zero status",
          "        posix        change the behavior of bash where the default",
          "                     operation differs from the Posix standard to",
          "                     match the standard",
          "        privileged   same as -p",
          "        verbose      same as -v",
          "        vi           use a vi-style line editing interface",
          "        xtrace       same as -x"
          },
          "-p  Turned on whenever the real and effective user ids do not match.",
          "    Disables processing of the $ENV file and importing of shell",
          "    functions.  Turning this option off causes the effective uid and",
          "    gid to be set to the real uid and gid.",
          "-t  Exit after reading and executing one command.",
          "-u  Treat unset variables as an error when substituting.",
          "-v  Print shell input lines as they are read.",
          "-x  Print commands and their arguments as they are executed.",
          "-B  the shell will perform brace expansion",
          "-C  If set, disallow existing regular files to be overwritten",
          "    by redirection of output.",
          "-E  If set, the ERR trap is inherited by shell functions.",
          "-H  Enable ! style history substitution.  This flag is on",
          "    by default when the shell is interactive.",
          "-P  If set, do not resolve symbolic links when executing commands",
          "    such as cd which change the current directory.",
          "-T  If set, the DEBUG and RETURN traps are inherited by shell functions.",
          "--  Assign any remaining arguments to the positional parameters.",
          "    If there are no remaining arguments, the positional parameters",
          "    are unset.",
          "-   Assign any remaining arguments to the positional parameters.",
          "    The -x and -v options are turned off.",
        }
    }
    Using + rather than - causes these flags to be turned off.  The
    flags can also be used upon invocation of the shell.  The current
    set of flags may be found in $-.  The remaining n ARGs are positional
    parameters and are assigned, in order, to $1, $2, .. $n.  If no
    ARGs are given, all shell variables are printed.

    Exit Status:
    Returns success unless an invalid option is given.
}
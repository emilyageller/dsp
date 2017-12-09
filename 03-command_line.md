# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

##### Navigation
- `pwd` : show current working directory path
- `mkdir` : create a directory
- `ls` : list files in current directory
- `cd` : change directory
- `ls -a` : list all contents, including hidden files and directories
- `ls -l` : lists all contents of a directory in long format
- `ls -t` : order files and directories by the time they were last modified
- commands starting with `-` are called options
- options can be combined like `ls -alt`. this lists all contents, including hidden files and directories, in long format, ordered by the date and time they were last modified
- `wc` : outputs number of lines, words and characters in txt file
##### Manipulation
- `cp` : copies the contents of the first argument(s) to the last. (these can be files or directories)
- `touch` : creates a new file inside the working directory
- `\*`: wildcard. when used alone, (eg `cp * mydir`) it selects all files in the working directory. another use: `m*.txt` selects all files in the working directory starting with `m` and ending with `.txt`
- 'mv' : move first argument(s) to last. (can also use `mv` to rename files. eg. `mv batman.txt spiderman.txt` moves `batman.txt` into `spiderman.txt`, and if `spiderman.txt` dne in the current directory, batman is renamed to spiderman
- `rm` : remove argument from working directory
- `rm -r` : (`-r` stands for recursive) deletes a directory and all child directories
##### Redirection
- `echo` accepts the string entered as standard input, and echoes it back as standard output
 - `stdin`: standard input : info inputted into the terminal through input device
 - `stdout`: standard output: output after a process is run
 - `stderr`: standard error: error message outputted by a failed process
- redirection reroutes `stdin` `stdout` and `stderr` to or from a different location
- `>` redirects `stdout` into a file. note that it copies over contents of file
- `cat` outputs contents of a file in form of `stdout`
- `>>` appends `stdout` to file
- `|` is a pipe. takes `stdout` of command on left and pipes it as `stdin` into the command on the ride
- `uniq` filters adjacent duplicant lines in a file
- `grep` stands for 'global regular expression print'. searches files for lines that matcha pattern and returns the results
- `grep -i` : makes command case insensitive
- `grep -R`: searches all files in a directory and oputs filenames and lines containing matched results )`-R` stands for recursive)
- `grep -Rl` returns names of files containing a match
- `sed` : like find and replace. `sed s/find/replace`. `s` stands for subsititute, `find` is the string to find, `replace` is the string to add in place. Note: this only replaces the first instance of `find` on a line.  To replace all instances, add `/g/` at the end.
##### Generalizations/Configurations
- The environment refers to the preferences and settings of the current user.
- The nano editor is a command line text editor used to configure the environment.
- `~/.bash_profile` is where environment settings are stored. You can edit this file with nano.
- environment variables are variables that can be used across commands and programs and hold information about the environment.
- `export VARIABLE="Value"` sets and exports an environment variable.
- `USER` is the name of the current user.
- `PS1` is the command prompt.
- `HOME` is the home directory. It is usually not customized.
- `PATH` returns a colon separated list of file paths. It is customized in advanced cases.
- `env` returns a list of environment variables.


---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

 


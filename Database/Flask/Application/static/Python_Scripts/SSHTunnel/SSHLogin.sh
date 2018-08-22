#!/usr/bin/expect -f
spawn ssh username@tsdb.eie.wits.ac.za -D 4242
expect "Password:"
send "password"
interact
# putty -ssh username@tsdb.eie.wits.ac.za -pw password -D 4242

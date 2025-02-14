#!/usr/bin/node
/* print second argument */

const argv = process.argv;
if (argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(argv[2]);
}

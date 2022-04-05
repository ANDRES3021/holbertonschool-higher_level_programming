#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  let iterator = 0;
  while (iterator < process.argv[2]) {
    console.log('C is fun');
    iterator += 1;
  }
}

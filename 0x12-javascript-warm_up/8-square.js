#!/usr/bin/node
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  let iterator = 0;
  while (iterator < process.argv[2]) {
    console.log('X'.repeat(process.argv[2]));
    iterator += 1;
  }
}

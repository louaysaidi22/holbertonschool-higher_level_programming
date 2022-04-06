#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('0');
} else {
  let big = process.argv[2];
  let secondbig = process.argv[3];
  if (secondbig > big) {
    [big, secondbig] = [secondbig, big];
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (process.argv[i] > secondbig) {
      if (process.argv[i] > big) {
        secondbig = big;
        big = process.argv[i];
      } else {
        secondbig = process.argv[i];
      }
    }
  }
  console.log(secondbig);
}

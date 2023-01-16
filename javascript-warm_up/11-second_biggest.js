#!/usr/bin/node
if (process.argv[2] === undefined || process.argv.length === 3) {
  console.log('0');
} else {
  let big = parseInt(process.argv[2]);
  let secondbig = parseInt(process.argv[3]);
  if (secondbig > big) {
    [big, secondbig] = [secondbig, big];
  }
  for (let i = 4; i < process.argv.length; i++) {
    if (parseInt(process.argv[i]) > secondbig) {
      if (parseInt(process.argv[i]) > big) {
        secondbig = big;
        big = parseInt(process.argv[i]);
      } else {
        secondbig = parseInt(process.argv[i]);
      }
    }
  }
  console.log(secondbig);
}

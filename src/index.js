const fs = require('fs');

const file1 = JSON.parse(fs.readFileSync('data.json'));
const file2 = JSON.parse(fs.readFileSync('data2.json'));

 const countIds = (data) => {
  const counts = {};
  for (let item of data) {
    const id = item.id;
    counts[id] = (counts[id] || 0) + 1;
  }
  return counts;
}

const count1 = countIds(file1);
const count2 = countIds(file2);

const diffs = {};
for (let id of Object.keys({...count1, ...count2})) {
  const countDiff = (count2[id] || 0) - (count1[id] || 0);
  if (countDiff === 1) {
    diffs[id] = '+1';
  } else if (countDiff === -1) {
    diffs[id] = '-1';
  } else if (countDiff > 1) {
    diffs[id] = `+${countDiff}`;
  } else if (countDiff < -1) {
    diffs[id] = countDiff;
  } else {
    diffs[id] = count1[id] || count2[id];
  }
}

for (let id in diffs) {
  console.log(`${id}: ${diffs[id]}`);
}

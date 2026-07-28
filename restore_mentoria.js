const fs = require('fs');

let oldContent = fs.readFileSync('old_diag.js', 'utf16le');
if (!oldContent.includes('mentoría')) {
    oldContent = fs.readFileSync('old_diag.js', 'utf8');
}

const match = oldContent.match(/mentoría:\s*\[[\s\S]*?\}\s*\],\s*brechas:/);
if (!match) {
    console.log("Not found in old_diag.js");
    process.exit(1);
}

const block = match[0].replace(/,\s*brechas:/, '');
console.log("Block length:", block.length);

let currentContent = fs.readFileSync('diagnostico_data.js', 'utf8');
if (currentContent.includes('mentoría:')) {
    console.log("Already in current file");
    process.exit(0);
}

currentContent = currentContent.replace('brechas: [', block + ',\n    brechas: [');
fs.writeFileSync('diagnostico_data.js', currentContent, 'utf8');
console.log("RESTORED!");

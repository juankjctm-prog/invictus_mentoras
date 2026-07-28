const fs = require('fs');

const oldContent = fs.readFileSync('old_diag.js', 'utf16le');
const mentoriaIndex = oldContent.indexOf('mentoria: [');
const brechasIndex = oldContent.indexOf('brechas: [');

if (mentoriaIndex === -1 || brechasIndex === -1) {
    console.log("Could not find boundaries");
    process.exit(1);
}

// Extract everything from mentoria: [ up to brechas: [
const block = oldContent.substring(mentoriaIndex, brechasIndex);
console.log("Extracted block of length", block.length);

let current = fs.readFileSync('diagnostico_data.js', 'utf8');

if (current.includes('mentoria: [')) {
    console.log("Mentoria already exists!");
    process.exit(0);
}

current = current.replace('brechas: [', block + 'brechas: [');
fs.writeFileSync('diagnostico_data.js', current, 'utf8');
fs.writeFileSync('../implementaciones/Mentadas/diagnostico_data.js', current, 'utf8');
fs.writeFileSync('../implementaciones/Mujeres mentoras/diagnostico_data.js', current, 'utf8');

console.log("Success!");

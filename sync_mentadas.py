import codecs
import json

# Read the correct data from mujeresMentorasData
with codecs.open('mujeresMentorasData.js', 'r', 'utf-8') as f:
    mm_content = f.read()

start_idx = mm_content.find('[')
end_idx = mm_content.rfind(']') + 1
mm_data = json.loads(mm_content[start_idx:end_idx])

correct_day1 = mm_data[0]

# Now read mentadasData
with codecs.open('mentadasData.js', 'r', 'utf-8') as f:
    md_content = f.read()

m_start = md_content.find('[')
m_end = md_content.rfind(']') + 1
md_data = json.loads(md_content[m_start:m_end])

# Overwrite reading and questions
md_data[0]["fase2_lectura"] = correct_day1["fase2_lectura"]
md_data[0]["fase4_recall"] = correct_day1["fase4_recall"]

# Save back
new_md_json = json.dumps(md_data, indent=2, ensure_ascii=False)
final_md = "const mentadasData = " + new_md_json + ";\n\nwindow.mentadasData = mentadasData;\n"

with codecs.open('mentadasData.js', 'w', 'utf-8') as f:
    f.write(final_md)

print("Mentoreadas updated to match exactly with Mentoras reading and questions.")

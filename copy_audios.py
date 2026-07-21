import os
import shutil
import re

base_dir = r"D:\Documents\Negocios\ASSINT\app\Invictus\invictus-web\Mapa espiritual"
mentadas_audio_dir = os.path.join(base_dir, "QA_TXT_Mentadas", "Audios")
mentoras_audio_dir = os.path.join(base_dir, "QA_TXT_Mentora", "Audios")
target_dir = os.path.join(base_dir, "Mujeres mentoras", "audios")

if not os.path.exists(target_dir):
    os.makedirs(target_dir)

def copy_and_rename_audios(source_dir, prefix):
    if not os.path.exists(source_dir):
        print(f"Directory not found: {source_dir}")
        return
        
    for filename in os.listdir(source_dir):
        if filename.endswith(".mp3"):
            # Extract day number
            match = re.search(r'D[ií]a\s*(\d+)', filename, re.IGNORECASE)
            if match:
                day_num = match.group(1)
                new_filename = f"{prefix}_dia_{day_num}.mp3"
                
                src_path = os.path.join(source_dir, filename)
                dst_path = os.path.join(target_dir, new_filename)
                
                shutil.copy2(src_path, dst_path)
                print(f"Copied {filename} -> {new_filename}")
            else:
                print(f"Could not extract day from {filename}")

copy_and_rename_audios(mentadas_audio_dir, "mentada")
copy_and_rename_audios(mentoras_audio_dir, "mentora")
print("Done copying audios.")

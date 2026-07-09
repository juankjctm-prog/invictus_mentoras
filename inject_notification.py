html_file = "Invictus_Mentoras.html"

with open(html_file, "r", encoding="utf-8") as f:
    content = f.read()

notify_func = """
<script>
function showRealtimeNotification(msg) {
    console.log("Notification: " + msg);
    alert(msg);
}
</script>
"""

if "function showRealtimeNotification" not in content:
    content = content.replace("</body>", notify_func + "\\n</body>")
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print("Injected showRealtimeNotification.")
else:
    print("Already injected.")

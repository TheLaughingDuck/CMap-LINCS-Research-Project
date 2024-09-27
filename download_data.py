import requests
import time

print("Initiating custom file download script, glhf\n")

# Specify path and local filename
path = "https://s3.amazonaws.com/macchiato.clue.io/builds/LINCS2020/geneinfo_beta.txt" #"https://s3.amazonaws.com/macchiato.clue.io/builds/LINCS2020/level3/level3_beta_trt_misc_n26428x12328.gctx"
local_filename = "geneinfo_beta.txt" #"level3_beta_trt_misc_n26428x12328.gctx"
print("Target file\n", path, "\n", sep="")
print("The file is being downloaded. Interrupt with [Ctrl+C].\n")

# Keep track of start time
start_time = time.time()

# Send get request for data
response = requests.get(path,  stream=True)

# Write data chunk by chunk
with open(local_filename, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        f.write(chunk)

# Write a status report for the user
print("Download completed. Status code:", response.status_code, "(That's good!)" if response.status_code == 200 else "")
print("Elapsed time:", round(time.time()-start_time), "seconds")
print("\nThe file is stored in\n", local_filename, sep="")
print("\nEnd of custom file download script, gg")
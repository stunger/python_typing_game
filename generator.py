import requests
import msvcrt
import time

# input seed value
t = input("Select Topic: ")

# get generated text
r = requests.post(
    "https://api.deepai.org/api/text-generator",
    data={
        'text': t,
    },
    headers={'api-key': '3bfce947-eb6c-44cb-8adf-901c9dad85bf'}
)
j = r.json()

# set variables
original_text = j["output"].replace("\n", "")
text_list = list(original_text)
char_count = 0
error_count = 0

print(original_text + "\n")

start = time.time()
for item in text_list:
	char_count = char_count + 1
	c = ''	
	while item != c:
		error_count = error_count + 1
		c = msvcrt.getch().decode("iso-8859-1")
		if c == chr(27):
			end = time.time()
			time_diff = end - start
			error_count = error_count - char_count
			print("\nTime:", time_diff)
			print("Chars Typed:", char_count)
			print("Errors:", error_count)
			exit()

	print(c, end="", flush=True)

end = time.time()
time_diff = end - start
error_count = error_count - char_count
print("\n\n------Finished------")
print("\nTime:", time_diff)
print("Chars Typed:", char_count)
print("Errors:", error_count)
exit()
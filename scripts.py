import socket
import re

word_freq_1 = {}
word_count_1 = 0
with open("home/data/IF.txt", "r") as f:
    for line in f:
        words = re.findall(r'\b\w+\b', line)
        word_count_1 += len(words)
        for word in words:
            if word in word_freq_1:
                word_freq_1[word] += 1
            else:
                word_freq_1[word] = 1

word_freq_2 = {}
word_count_2 = 0
with open("home/data/AlwaysRememberUsThisWay.txt", "r") as f:
    for line in f:
        words = re.findall(r'\b\w+\b', line)
        # Now, we'll manually split contractions like "I'm" -> ["I", "am"]
        expanded_words = []
        for word in words:
            # Split contractions like "I'm" -> ["I", "am"]
            if "'" in word:
                expanded_words.extend(word.split("'"))
            else:
                expanded_words.append(word)

        word_count_2 += len(expanded_words)
        for word in expanded_words:
            if word in word_freq_2:
                word_freq_2[word] += 1
            else:
                word_freq_2[word] = 1


total_word_count = word_count_1 + word_count_2

with open("home/data/output/results.txt", "w") as f:
    f.write(f"Total word count: {total_word_count}\n\n")

    f.write("Word frequency for IF.txt:\n")
    for word, freq in word_freq_1.items():
        f.write(f"{word}: {freq}\n")

    f.write("\n")

    f.write("Word frequency for AlwaysRememberUsThisWay.txt:\n")
    for word, freq in word_freq_2.items():
        f.write(f"{word}: {freq}\n")

with open("home/data/output/results.txt", "r") as f:
    print(f.read())

# Try to connect to the host machine using the host.docker.internal alias
host_ip = socket.gethostbyname("host.docker.internal")

print(f"Host machine IP address: {host_ip}")

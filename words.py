import argparse
import os
import string


def main():
    parser = argparse.ArgumentParser('words')
    parser.add_argument(
        '-i', '--in', help='Path to wiki abstracts file', type=str, required=True)
    parser.add_argument(
        '-o', '--out', help='Output file path', type=str, required=True)
    args = parser.parse_args()
    frequencies = {}
    wiki_dump = open(getattr(args, 'in'), mode='r', encoding='utf-8')
    for line in wiki_dump:
        if line.find('<abstract>') == 0:
            abstract = line.lower().replace('<abstract>', '').replace('</abstract>', '').strip()
            # Skip empty abstracts
            if len(abstract) == 0:
                continue
            # Skip non useful (for our purposes) abstracts
            if abstract[0] not in string.ascii_lowercase:
                continue
            # Skip very common abstracts
            if abstract.find('was a common year') >= 0:
                continue
            # Sanitize the abstract
            sanitized_abstract = ''
            for char in abstract:
                if char in string.ascii_lowercase or char == ' ':
                    sanitized_abstract += char
            # Remove very common Wikipedia phrases
            sanitized_abstract = sanitized_abstract.replace('may mean', '')
            sanitized_abstract = sanitized_abstract.replace('can refer to', '')
            sanitized_abstract = sanitized_abstract.replace('may refer to', '')
            sanitized_abstract = sanitized_abstract.replace(
                'often refers to', '')
            sanitized_abstract = sanitized_abstract.replace(
                'american english', '')
            sanitized_abstract = sanitized_abstract.replace(
                'british english', '')
            sanitized_abstract = sanitized_abstract.replace(
                'canadian english', '')
            sanitized_abstract = sanitized_abstract.replace(
                'australian english', '')
            # Skip one word sanitized abstracts
            if len(sanitized_abstract.strip().split(' ')) == 1:
                continue
            # Count words
            words = sanitized_abstract.split(' ')
            for word in words:
                word = word.strip()
                # Some words are blank because of multiple spaces
                if word == '':
                    continue
                # Letters are not words
                if len(word) == 1:
                    continue
                if word in frequencies:
                    frequencies[word] += 1
                else:
                    frequencies[word] = 1
    wiki_dump.close()
    # Output CSV
    output = open(args.out, mode='w', encoding='utf-8')
    output.write('Word,Frequency')
    output.write(os.linesep)
    for word in sorted(frequencies, key=frequencies.get, reverse=True):
        output.write(word + ',' + str(frequencies[word]))
        output.write(os.linesep)
    output.close()


if __name__ == '__main__':
    main()

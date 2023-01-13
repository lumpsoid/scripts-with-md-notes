import os
import re

space_at_the_end = re.compile(r'\s+$')
del_hashtagh = re.compile(r'#')
del_comma = re.compile(r', ')
pair_of_col = re.compile(r'::')
change_tag = re.compile(r'^tags:')

def note_processing(path_to_file, note, file_less_two=0, not_tag=0, tag_process=0, write=0):
    if file_less_two:
        note.append('tag: N')
        note[0] = space_at_the_end.sub('', note[0]) + '\n'
    elif not_tag:
        new_file = []
        for index in range(len(note)):
            if index == 1:
                new_file.append('tag: N\n')
                new_file.append(note[index])
                continue
            new_file.append(note[index])
        note = list(new_file)
    elif tag_process:
        tag_line = note[1]
        tag_line = del_hashtagh.sub('', tag_line)
        tag_line = del_comma.sub(' ', tag_line)
        tag_line = pair_of_col.sub(':', tag_line)
        tag_line = change_tag.sub('tag:', tag_line)
        note[1] = tag_line
    if write:
        with open(path_to_file, mode="w", encoding='utf-8') as f:
            f.write("".join(note))


def slide_on_notes(dir_path):
    with os.scandir(dir_path) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.md'):
                file_path = os.path.join(dir_path, entry.name)  # use os.path.join()
                with open(file_path, encoding='utf-8') as f:
                    full_file = f.readlines()
                if len(full_file) < 2:
                    note_processing(file_path, full_file, file_less_two=1, write=1)
                elif not "tags" in full_file[1]:
                    note_processing(file_path, full_file, not_tag=1, write=1)
                else:
                    note_processing(file_path, full_file, tag_process=1, write=1)
    print('Script is done')

if __name__ == "__main__":
    slide_on_notes(dir_path='/home/qq/Documents/i')
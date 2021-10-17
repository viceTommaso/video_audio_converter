# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from __future__ import unicode_literals
import json
import os
import shutil
import sys
import youtube_dl


boold = False


def ren(t_directory, t_before, t_after):
    """
    rename file that are in t_directory with specificated argoments
    :param t_directory: directory
    :param t_before: to replace
    :param t_after: replace by
    :return: 0
    """
    for root, dirs, files in os.walk(t_directory):
        for i in files:
            if i != __file__:
                v_file = i.split(".")
                st = ""
                for s in v_file[:-1]:
                    if s != v_file[-2]:
                        st += f"{s}."
                    else:
                        st += s
                os.rename(os.path.join(root, i), os.path.join(root, f"{st.replace(t_before, t_after)}.{v_file[-1]}"))
    return 0


def error_char(t_directory, action):
    """
    rename file that cause error with other words
    :param t_directory: directory
    :param action: "ren" for rename, "undo" for undo
    :return: 0
    """
    char, repl = [" ", "&"], ["#$#", "EspEc"]      #caratteri che danno errore con quello che li sostituisce

    if action == "ren":
        count = 0
        for i in range(0, len(char)):
            ren(t_directory, char[count], repl[count])
            count += 1
    if action == "undo":
        count = 0
        for i in range(0, len(char)):
            ren(t_directory, repl[count], char[count])
            count += 1
    return 0


def video(p_0, p_2, p_3, p_10, i_type):
    """
    downloading operations
    :param p_0:input
    :param p_2:download_video
    :param p_3:remove_str_file
    :param p_10:e_dir_video
    :param i_type:type of input, string("s")/file("f")
    :return: 0
    """
    if p_2 == "T":
        if i_type == "f":
            with open(p_0, "r", encoding="utf-8") as f_link:
                for i in f_link:
                    os.system(f"""cd {p_10} && youtube-dl -f best {i}""")
        elif i_type == "s":
            os.system(f"""cd {p_10} && youtube-dl -f best {p_0}""")
        else:
            print("inserire un tipo di input valido (s/f)")
            pass

    if p_3 == "T":
        for root, dirs, files in os.walk(p_10):
            for i in files:
                if i != __file__:
                    v_file = i.split(".")
                    st = ""
                    for s in v_file[:-1]:
                        if s != v_file[-2]:
                            st += f"""{s}."""
                        else:
                            st += f"""{s}"""
                    os.rename(os.path.join(root, i), os.path.join(root, f"""{st.replace(st[-12:], "")}.{v_file[-1]}"""))
    return 0


def convert(p_1, p_5, p_6, p_7, p_8, p_10, p_11):
    """
    conversions operations
    :param p_1:audio_quality
    :param p_5:convert_video
    :param p_6:convert_existing_video
    :param p_7:delete_converted_video
    :param p_8:dir_video
    :param p_10:e_dir_video
    :param p_11:e_dir_audio
    :return: 0
    """
    if p_6 == "T":
        for root, dirs, files in os.walk(p_8):
            for i in files:
                try:
                    shutil.move(os.path.join(root, i), p_10)
                except shutil.Error:
                    print("\n\n\nFile con lo stesso nome già presente: file non elaborato\n(file preesistente)\n\n\n")
                    pass

    if p_5 == "T":
        error_char(p_10, "ren")
        for root, dirs, files in os.walk(p_10):
            for i in files:
                v_i = i.split(".")
                st = ""
                for s in v_i[:-1]:
                    if s != v_i[-2]:
                        st += f"{s}."
                    else:
                        st += s
                os.system(f"""ffmpeg -i .\\{p_10}\\{i} -acodec libmp3lame -b:a {p_1} -vn .\\{p_11}\\{st}.mp3""")

                if p_7 == "T":
                    os.remove(os.path.join(root, i))

        if p_7 != "T":
            error_char(p_10, "undo")
        error_char(p_11, "undo")
    return 0


def move_files(original_path, destination_path):
    """
    end operations
    :param original_path:where are files
    :param destination_path:where files goes
    :return: 0
    """
    for root, dirs, files in os.walk(original_path):
        for i in files:
            shutil.copy(os.path.join(root, i), destination_path)
            os.remove(os.path.join(root, i))
    return 0


def init_files(file_ck, file_name):
    """
    check if there are any files needed to boot
    :param file_ck:file to check if exist
    :param file_name:the name to print when crated
    :return: 0
    """
    if str(os.path.exists(file_ck)) == "False":
        with open(file_ck, "a", encoding="utf-8") as f_link:
            pass
        print(f"""{file_name} FILE doesn't exist, just created""")
    return 0


def init_directory(dir_ck, dir_vsby, dir_name):
    """
    check if there are any dirs needed to boot
    :param dir_ck:directory to check if exist
    :param dir_vsby:if directory is visible or not (any str/h)
    :param dir_name:the name to print when crated
    :return: 0
    """
    if str(os.path.exists(dir_ck)) == "False":
        os.mkdir(dir_ck)
        msg = f"""{dir_name} DIRECTORY doesn't exist, just created"""
        if dir_vsby == "h":
            os.system(f"""attrib +h {dir_ck}""")
            msg = msg + " and hidden"
        print(msg)
    return 0


def main():
    """
    main
    :return: 0
    """
    if boold:
        print("start")

    with open("settings.json", "r", encoding="utf-8") as file_json:
        settings = json.loads(file_json.read())

    parm = (settings["file_input_link"],
            settings["audio_quality"],
            settings["download_video"],
            settings["remove_str_file"],
            settings["reset_file_input"],
            settings["convert_video"],
            settings["convert_existing_video"],
            settings["delete_converted_video"],
            settings["dir_video"],
            settings["dir_audio"],
            settings["e_dir_video"],
            settings["e_dir_audio"])

    init_files(parm[0], "INPUT")
    init_directory(parm[8],"", "VIDEO")
    init_directory(parm[9],"", "AUDIO")
    init_directory(parm[10],"h", "HIDE VIDEO")
    init_directory(parm[11],"h", "HIDE AUDIO")

    move_files(parm[10], parm[8])
    move_files(parm[11], parm[9])

    if len(sys.argv) >= 2:
        video(sys.argv[-1], parm[2], parm[3], parm[10], "s")
    else:
        video(parm[0], parm[2], parm[3], parm[10], "f")
        if parm[4] == "T":
            with open(parm[0], "w", encoding="utf-8") as f_link:
                pass

    convert(parm[1], parm[5], parm[6], parm[7], parm[8], parm[10], parm[11])

    move_files(parm[10], parm[8])
    move_files(parm[11], parm[9])

    if boold:
        print("end")
    return 0


if __name__ == "__main__":
    main()

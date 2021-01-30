# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from __future__ import unicode_literals
import json
import os
import shutil
import sys
import youtube_dl


boold = False


with open("settings.json", "r", encoding="utf-8") as file_json:
    settings = json.loads(file_json.read())


def ren(t_directory, t_before, t_after):
    """
    rename file whit specificated argoments
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


def convert():
    """
    conversions operations
    :return: 0
    """
    if settings["convert_existing_video"] == "T":
        for root, dirs, files in os.walk(settings["dir_video"]):
            for i in files:
                shutil.move(os.path.join(root, i), settings["e_dir_video"])

    if settings["convert_video"] == "T":
        ren(settings["e_dir_video"], settings["before"], settings["after"])
        ren(settings["e_dir_video"], "&", "EspEc")
        for root, dirs, files in os.walk(settings["e_dir_video"]):
            for i in files:
                v_i = i.split(".")
                st = ""
                for s in v_i[:-1]:
                    if s != v_i[-2]:
                        st += f"{s}."
                    else:
                        st += s
                os.system(
                    f"""ffmpeg -i .\\{settings["e_dir_video"]}\\{i} -acodec libmp3lame -b:a {settings["audio_quality"]} -vn .\\{settings["e_dir_audio"]}\\{st}.mp3""")

                if settings["delete_converted_video"] == "T":
                    os.remove(os.path.join(root, i))

        if settings["delete_converted_video"] != "T":
            ren(settings["e_dir_video"], settings["after"], settings["before"])
            ren(settings["e_dir_video"], "EspEc", "&")
        ren(settings["e_dir_audio"], settings["after"], settings["before"])
        ren(settings["e_dir_audio"], "EspEc", "&")
    return 0


def res():
    """
    end operations
    :return: 0
    """
    for root, dirs, files in os.walk(settings["e_dir_video"]):
        for i in files:
            shutil.copy(os.path.join(root, i), settings["dir_video"])
            os.remove(os.path.join(root, i))

    for root, dirs, files in os.walk(settings["e_dir_audio"]):
        for i in files:
            shutil.copy(os.path.join(root, i), settings["dir_audio"])
            os.remove(os.path.join(root, i))
    return 0


def init():
    """
    check if there are any files needed to boot
    :return: 0
    """
    if str(os.path.exists(settings["file_input_link"])) == "False":
        with open(settings["file_input_link"], "a", encoding="utf-8") as f_link:
            pass
        print("INPUT FILE doesn't exist, just created")

    if str(os.path.exists(settings["dir_video"])) == "False":
        os.mkdir(settings["dir_video"])
        print("VIDEO DIRECTORY doesn't exist, just created")
    
    if str(os.path.exists(settings["dir_audio"])) == "False":
        os.mkdir(settings["dir_audio"])
        print("AUDIO DIRECTORY doesn't exist, just created")

    if str(os.path.exists(settings["e_dir_video"])) == "False":
        os.mkdir(settings["e_dir_video"])
        os.system(f"""attrib +h {(settings["e_dir_video"])}""")
        print("HIDE VIDEO DIRECTORY doesn't exist, just created")
    
    if str(os.path.exists(settings["e_dir_audio"])) == "False":
        os.mkdir(settings["e_dir_audio"])
        os.system(f"""attrib +h {(settings["e_dir_audio"])}""")
        print("HIDE AUDIO DIRECTORY doesn't exist, just created")
    return 0


def main():
    """
    main
    :return: 0
    """
    if boold:
        print("start")

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
            settings["e_dir_audio"],
            settings["before"],
            settings["after"])

    init()
    res()
    if len(sys.argv) >= 2:
        video(sys.argv[-1], parm[2], parm[3], parm[10], "s")
    else:
        video(parm[0], parm[2], parm[3], parm[10], "f")
        if parm[4] == "T":
            with open(parm[0], "w", encoding="utf-8") as f_link:
                pass
    convert()
    res()

    if boold:
        print("end")

    return 0


if __name__ == "__main__":
    main()

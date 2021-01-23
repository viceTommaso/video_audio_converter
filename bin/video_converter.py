# -*- coding: utf-8 -*-
# !/usr/bin/env python3

from __future__ import unicode_literals
import json
import os
import shutil
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


def video():
    """
    downloading operations
    :return: 0
    """
    if settings["download_video"] == "T":
        with open(settings["file_input_link"], "r", encoding="utf-8") as f_link:
            for i in f_link:
                os.system(f"""cd {settings["e_dir_video"]} && youtube-dl -f best {i}""")

    if settings["remove_str_file"] == "T":
        for root, dirs, files in os.walk(settings["e_dir_video"]):
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


def main():
    """
    main
    :return: 0
    """
    if boold:
        print("start")

    if str(os.path.exists(settings["file_input_link"])) == "False":
        with open(settings["file_input_link"], "a", encoding="utf-8") as f_link:
            pass
        print("file doesn't exist, just created")

    res()
    video()
    if settings["reset_file_input"] == "T":
        with open(settings["file_input_link"], "w", encoding="utf-8") as f_link:
            pass
    convert()
    res()

    if boold:
        print("end")

    return 0


if __name__ == "__main__":
    main()

#!/usr/bin/env bash

AUDIO_DEST="/Volumes/OCTATRACK/SET/AUDIO"
AUDIO_SRC="./OCTATRACK_out/OCTATRACK/*"

# Backup what the audio

cp -R $AUDIO_DEST AUDIO_bak_`date +"%Y-%m-%d.%H-%M"`

# Remove the old audio

rm -rf $AUDIO_DEST/*

# copy in the new audio

cp -RL $AUDIO_SRC $AUDIO_DEST

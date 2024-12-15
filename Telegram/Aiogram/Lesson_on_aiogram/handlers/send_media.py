from aiogram.types import Message, FSInputFile, InputMediaPhoto, InputMediaVideo, InputMediaAudio
from aiogram import Bot
import os
from aiogram.utils.chat_action import ChatActionSender


async def get_audio(message: Message, bot: Bot):
    audio = FSInputFile(path=os.path.join(r'files_for_bot\Toby_Keith_-_American_Soldier_48120369.mp3'),
                        filename='Американский солдат')
    await bot.send_audio(message.chat.id, audio=audio)


async def get_photo(message: Message, bot: Bot):
    photo = FSInputFile(path=os.path.join(r'files_for_bot\soldier.jpg'))
    await bot.send_photo(message.chat.id, photo)


async def get_media_group(message: Message, bot: Bot):
    photo1 = InputMediaPhoto(type='photo', media=FSInputFile(os.path.join(r'files_for_bot\girl1.jpg')))
    photo2 = InputMediaPhoto(type='photo', media=FSInputFile(os.path.join(r'files_for_bot\girl2.jpg')))
    photo3 = InputMediaPhoto(type='photo', media=FSInputFile(os.path.join(r'files_for_bot\girl3.jpg')))
    photo4 = InputMediaPhoto(type='photo', media=FSInputFile(os.path.join(r'files_for_bot\girl4.jpg')))
    video = InputMediaVideo(type='video', media=FSInputFile(os.path.join(r'files_for_bot\video_girl.mp4')))
    media = [video, photo1, photo2, photo3, photo4]
    await bot.send_media_group(message.chat.id, media)


async def get_audio_playlist1(message: Message, bot: Bot):
    track_1 = InputMediaAudio(type='audio', media=FSInputFile(os.path.join(r'files_for_bot\Slipknot_-_Before_I_Forget_47954384.mp3')))
    track_2 = InputMediaAudio(type='audio', media=FSInputFile(os.path.join(r'files_for_bot\Slipknot_-_Duality_47954348.mp3')))
    track_3 = InputMediaAudio(type='audio', media=FSInputFile(os.path.join(r'files_for_bot\Slipknot_-_People_Shit_47954341.mp3')))
    track_4 = InputMediaAudio(type='audio', media=FSInputFile(os.path.join(r'files_for_bot\Slipknot_-_Psychosocial_47954346.mp3')))
    track_5 = InputMediaAudio(type='audio', media=FSInputFile(os.path.join(r'files_for_bot\Slipknot_-_Unsainted_64305760.mp3')))
    media = [track_1, track_2, track_3, track_4, track_5]
    await bot.send_media_group(message.chat.id, media)


async def get_sticker(message: Message, bot: Bot):
    sticker = FSInputFile(path=os.path.join(r'files_for_bot\sticker1.jpg'))
    await bot.send_sticker(message.chat.id, sticker)


async def get_video(message: Message, bot: Bot):
    async with ChatActionSender.upload_video(chat_id=message.chat.id, bot=bot):
        video = FSInputFile(path=os.path.join(r'files_for_bot\video_girl.mp4'))
        await bot.send_video(message.chat.id, video)


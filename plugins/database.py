#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument


import asyncio
import motor.motor_asyncio

# Set up MongoDB client and database
URL = "mongodb+srv://admin:rahul@mydatabase.zu1yt8m.mongodb.net/?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(URL)
db = client["telegram_channels"]

web_col = db["web_channel_ids"]
desi_col = db["desi_channel_ids"]
ignore_col = db["ignore_ids"]
all_col = db["channel_ids"]


async def add_ignore_id(channel_id):
    channel_id = int(channel_id)
    new_channel = {
        "_id": channel_id}
    try:
        await ignore_col.insert_one(new_channel)
    except:
        pass


# Function to add new channel IDs to the list
async def add_channel_id(category, channel_id, app):
    channel_id = int(channel_id)
    chat = await app.get_chat(channel_id)
    title = chat.title
    subs = chat.members_count
    try:
        pic = chat.photo.big_file_id
    except:
        pic = None
    link = chat.invite_link
    username = chat.username
    new_channel = {
        "_id": channel_id,
        "TITLE": title,
        "SUBS": subs,
        "PROFILE_PIC": pic,
        "LINK": link,
        "USERNAME": username
    }

    try:
        await category.insert_one(new_channel)
        await all_col.insert_one(new_channel)

    except:
        pass

# Function to retrieve channel info
async def get_chat_info(channel_id):
    try:
        channel_id = int(channel_id)

        # Search the collection for the document with the specified channel_id
        query = {"_id": channel_id}
        result = await all_col.find_one(query)

        # Extract the desired fields from the document
        title = result["TITLE"]
        link = result["LINK"]
        pic = result["PROFILE_PIC"]
        subs = result["SUBS"]
        username = result["USERNAME"]

        output = f"Title: {title}\nLink: {link}\nProfile Pic: {pic}\nUsername: @{username}\nSubscribers: {subs}"

        return output

    except Exception as e:
        print(f"Error retrieving channel info: {e}")
        return "No Info Found"

# Function to retrieve all channel info


async def get_all_chat_info(category):
    try:
        count = 1
        total_subs = 0
        text = 'You have {} channels:\n\n'
        channel_info = []
        async for channel in category.find():
            # print(channel)
            subs = channel["SUBS"]
            total_subs += subs
            chat_id = channel["_id"]
            chat_info = f"#{count} `{chat_id}` {subs}"
            channel_info.append(chat_info)
            count += 1

        subs_text = f"Total Channels Subs: `{total_subs}`"

        
        return text.format(count-1), channel_info, subs_text

    except Exception as e:
        print(f"Error retrieving channel info: {e}")
        return "No Info Found"

# Function to delete channel IDs from the list


async def delete_channel_id(category, channel_id):
    delete_query = {"_id": int(channel_id)}
    await category.delete_one(delete_query)

# Function to retrieve all channel IDs in the list


async def get_all_channel_ids(category):
    channel_ids = []
    async for channel in category.find():
        channel_ids.append(channel["_id"])
    return channel_ids

# # Example usage:
# async def main():
#     # Call the asynchronous functions here

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

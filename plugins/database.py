#!/usr/bin/env python3
# pylint: disable=missing-docstring,unused-import,invalid-name,wildcard-import,unused-wildcard-import,broad-exception-caught,bare-except,unused-argument


import asyncio
import motor.motor_asyncio

# Set up MongoDB client and database
URL = "mongodb+srv://admin:rahul@mydatabase.zu1yt8m.mongodb.net/?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(URL)
db = client["Kdviferforwrder_bot"]


categories = db["categories"]
all_col = db["channel_ids"]


async def get_all_cats():
    cats_names = []
    async for cat in categories.find():
        cat_name = cat["title"]
        cat_id = cat["_id"]
        dictionary = {"_id": cat_id, "title": cat_name}

        cats_names.append(dictionary)

    return cats_names


async def update_by_id(cat_id, channel_id):
    try:
        data = await show_category(cat_id)
        chats_list = data["chat_ids"]
        chats_list.append(int(channel_id))

        update_operation = {
            "$set": {
                "chat_ids": chats_list}}

        await categories.update_one({"_id": int(cat_id)}, update_operation)
    except:
        pass


async def remove_by_id(cat_id, channel_id):
    try:
        data = await show_category(cat_id)
        chats_list = data["chat_ids"]
        chats_list.remove(int(channel_id))

        update_operation = {
            "$set": {
                "chat_ids": chats_list}}

        await categories.update_one({"_id": int(cat_id)}, update_operation)
    except:
        pass


async def is_more_than_n_collections(n=9):
    try:
        # List the collection names in the database
        collection_names = await db.list_collection_names()

        # Check if there are more than n collections
        return len(collection_names) > n

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


async def get_collection_names():
    # List the collection names in the database
    collection_names = await db.list_collection_names()

    return collection_names


async def make_new_collect(title):
    new_category = db[title]
    return title


async def add_category(channel_id, title):
    channel_id = int(channel_id)
    new_channel = {
        "_id": channel_id,
        "title": title,
        "chat_ids": []}
    try:
        await categories.insert_one(new_channel)
    except:
        pass


async def show_category(channel_id):
    query = {"_id": int(channel_id)}
    result = await categories.find_one(query)
    return result


async def add_ignore_id(channel_id):
    channel_id = int(channel_id)
    new_channel = {
        "_id": channel_id}
    try:
        await categories.insert_one(new_channel)
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
    channel_info = []
    count = 1
    if category == ignore_col:
        async for channel in category.find():
            chat_id = channel["_id"]
            chat_info = f"#{count} `{chat_id}`"
            channel_info.append(chat_info)
            count += 1
        return channel_info

    try:
        total_subs = 0
        text = 'You have {} channels:\n\n'

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

    except:
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

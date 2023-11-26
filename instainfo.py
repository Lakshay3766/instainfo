import instaloader
import sys
from instaloader import Instaloader

def insta_info_banner():
    print("""
INSTA INFO
\033[41m=[===> Insta Info | https://github.com/lakshaymadaan3766 <===]=\n\033[0m""")
insta_info_banner()

x = Instaloader()

try:
    uname = input("\033[36mEnter an Instagram username \033[0m: \033[36m")
    if uname == "":
        print("\033[33mUnknown command!")
        sys.exit()

    f = instaloader.Profile.from_username(x.context, uname)

    print("\033[32mUsername\033[0m :", f.username)
    print("\033[32mID\033[0m :", f.userid)
    print("\033[32mFull Name\033[0m :", f.full_name)
    print("\033[32mBiography\033[0m :", f.biography)
    print("\033[32mBusiness Category Name\033[0m :", f.business_category_name)
    print("\033[32mExternal URL\033[0m :", f.external_url)
    print("\033[32mFollowed by Viewer\033[0m :", f.followed_by_viewer)
    print("\033[32mFollowees\033[0m :", f.followees)
    print("\033[32mFollowers\033[0m :", f.followers)
    print("\033[32mFollows Viewer\033[0m :", f.follows_viewer)
    print("\033[32mBlocked by Viewer\033[0m :", f.blocked_by_viewer)
    print("\033[32mHas Blocked Viewer\033[0m :", f.has_blocked_viewer)
    print("\033[32mHas Highlight Reels\033[0m :", f.has_highlight_reels)
    print("\033[32mHas Public Story\033[0m :", f.has_public_story)
    print("\033[32mHas Requested Viewer\033[0m :", f.has_requested_viewer)
    print("\033[32mRequested by Viewer\033[0m :", f.requested_by_viewer)
    print("\033[32mHas Viewable Story\033[0m :", f.has_viewable_story)
    print("\033[32mIGTV\033[0m :", f.igtvcount)
    print("\033[32mBusiness Account\033[0m :", f.is_business_account)
    print("\033[32mPrivate Account\033[0m :", f.is_private)
    print("\033[32mVerified\033[0m :", f.is_verified)
    print("\033[32mMedia Count\033[0m :", f.mediacount)
    print("\033[32mProfile Picture URL\033[0m :", f.profile_pic_url)

except KeyboardInterrupt:
    print("\033[33mI understand!")

except EOFError:
    print("\033[33mWhy?")

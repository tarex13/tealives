// JavaScript source code
var actions =
    '<div class="post-actions">' +
    '<a href="javascript:void(0)" class="post-action" onclick="heartClicked(event)">' +
    '<svg stroke="currentColor" stroke-width="2" class="heart" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24">' +
    '<path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z" />' +
    '</svg>' +
    '<span class="post-likes"></span>' +
    '</a>' +
    '<a href="javascript:void(0)" class="post-action new" onclick="commentClicked(event)">' +
    '<svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">' +
    '<path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z" />' +
    '</svg>' +
    '<span class="post-comments"></span>' +
    '</a>' +
    '<a href="javascript:void(0)" class="post-action">' +
    '<svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24">' +
    '<path d="M17 1l4 4-4 4" />' +
    '<path d="M3 11V9a4 4 0 014-4h14M7 23l-4-4 4-4" />' +
    '<path d="M21 13v2a4 4 0 01-4 4H3" />' +
    '</svg>' +
    '13' +
    '</a>' +
    '</div>';

var commActions =
    '<div class="post-actions"><a href="javascript:void(0)" class="post-action" onclick="heartClicked(event)"><svg stroke="currentColor" stroke-width="2" class="heart" fill="none" stroke-linecap="round" stroke-linejoin="round" viewBox="0 0 24 24"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"></path></svg><span class="post-likes">1</span></a><a href="javascript:void(0)" class="post-action new" onclick="commentClicked(event)"><svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"></path></svg>20</a><a href="javascript:void(0)" class="post-action"><svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24"><path d="M17 1l4 4-4 4"></path><path d="M3 11V9a4 4 0 014-4h14M7 23l-4-4 4-4"></path><path d="M21 13v2a4 4 0 01-4 4H3"></path></svg>13</a></div>'; 

var head =
    '<div class="post-cont">' +
    '<div class="post box">' +
    '<div class="post-main">' +
    '<div class="prof-pic-cont post_image animated-bg">' +
    '<!-- <img src="https://images.genius.com/2326b69829d58232a2521f09333da1b3.1000x1000x1.jpg" class="prof-pic" /> -->' +
    '</div>' +
    '<div class="post-detail">' +
    '<div class="post_detail_tab"><strong>{{ db.username }}</strong><span>My time out</span></div>' +
    '<div class="post-date">6 hours ago</div>' +
    '</div>' +
    '<div id="intro-menu" onclick="hideUnhideContextMenu(this)">' +
    '<button class="intro-menu"></button>' +
    '<button class="intro-menu"></button>' +
    '<button class="intro-menu"></button>' +
    '</div>' +
    '</div>' +
    '<div class="context-menu hidden">' +
    '<div class="context-item"><div class="context-name">User</div><div class="context-more">></div></div>' +
    '<div class="context-item"><div class="context-name">Post</div><div class="context-more">></div></div>' +
    '<!-- <div class="edit">Use Template</div>' +
    '<div class="edit">Edit Post</div>' +
    '<div class="">Unfollow / Follow User</div>' +
    '<div class="">Report Post</div>' +
    '<div class="">Show similar</div>' +
    '<div class="">Block Post / User</div>' +
    '<div class="">Share</div>' +
    '<div class="">Copy Link</div>' +
    '<div class="">Embed</div> -->' +
    '<div class="context-item context-name close" onclick="hideUnhideContextMenu(this)">Close</div>' +
    '</div>';

var comment = '<div class="comment box">' +
    '    <div class="comment-top">' +
    '        <div class="back" onclick="commentClicked(event)">' +
    '                <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" height="72pt" version="1.1" viewBox="0 0 72 72" width="72pt">' +
    '                    <defs>' +
    '                        <style type="text/css">' +
    '                            * {' +
    '                                stroke-linecap: butt;' +
    '                                stroke-linejoin: round;' +
    '                           }.back{cursor: pointer}' +
    '                        </style>' +
    '                   </defs>' +
    '                   <g id="figure_1">' +
    '                        <g id="patch_1">' +
    '                            <path d="M 0 72  L 72 72  L 72 0  L 0 0  z " style="fill:none;opacity:0;" />' +
    '                        </g>' +
    '                        <g id="text_1">' +
    '                            <path d="M 65.144375 35.006875  C 65.144375 32.425 63.43375 30.15125 60.703125 30.15125  L 33.991875 30.15125  L 45.105625 19.0375  C 46.019375 18.12375 46.550625 16.87 46.550625 15.584375  C 46.550625 14.288125 46.019375 13.034375 45.105625 12.13125  L 42.258125 9.315625  C 41.344375 8.4125 40.133125 7.88125 38.8475 7.88125  C 37.55125 7.88125 36.2975 8.4125 35.394375 9.315625  L 10.69125 33.986875  C 9.82 34.900625 9.28875 36.14375 9.28875 37.44  C 9.28875 38.725625 9.82 39.979375 10.69125 40.850625  L 35.394375 65.59625  C 36.2975 66.4675 37.55125 66.99875 38.8475 66.99875  C 40.133125 66.99875 41.386875 66.4675 42.258125 65.59625  L 45.105625 62.70625  C 46.019375 61.835 46.550625 60.58125 46.550625 59.295625  C 46.550625 58.01 46.019375 56.75625 45.105625 55.885  L 33.991875 44.72875  L 60.703125 44.72875  C 63.43375 44.72875 65.144375 42.444375 65.144375 39.8625  z " />' +
    '                       </g>' +
    '                   </g>' +
    '                </svg>' +
    '            </div>' +
    '            <div class="comment-text">Comments</div>' +
    '            <div class="comments-count">' +
    '                <svg stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round" class="css-i6dzq1" viewBox="0 0 24 24"><path d="M21 15a2 2 0 01-2 2H7l-4 4V5a2 2 0 012-2h14a2 2 0 012 2z"></path></svg>' +
    '               250k' +
    '            </div>' +
    '       </div>' +
    '       <div class="comment-body">' +
    '</div > ' +
    '    <div class="comment-bottom">' +
    '       <input class="comment-input" oninput="cTyping(event)" placeholder="Add a comment..." />' +
    '      <button type="submit" class="send">Send</button>' +

    '</div> ' +
    '</div>';

var ctext = '<div class="comment-text"><label class="comment-user"></label><label class="comm-text"></label>' + commActions + '</div>';

var temp1 =
    '<!--Template 1-->' +
    head +
    '<div class="post-content temp1" > ' +
    '<!--When the bass drops, so do my problems.--> ' +
    '<div class="post-files" > ' +
    '<div class="file_left post_image post_file post_file_left animated-bg"> ' +
    '<!--< img src = "https://images.unsplash.com/photo-1508179719682-dbc62681c355?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2378&q=80" alt = "" class="post-file_left"/> -->' +
    '</div > ' +
    '<div class="post-right" > ' +
    '<div class="file-right post_image file_right_up animated-bg" ><!--< img src = "https://images.unsplash.com/photo-1502872364588-894d7d6ddfab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80" alt = "" class="post-file" /> --></div > ' +
    '<div class="file-right post_image file_right_down animated-bg" ><!--< img src = "https://images.unsplash.com/photo-1566737236500-c8ac43014a67?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80" alt = "" class="post-file" /> --></div > ' +
    '</div>' +
    '</div>' +
    '</div>' +
    actions +
    '</div > ' + comment
    ;
var temp2 =
    '<!--Template 2-->' +
    head +
    '<div class="post-content temp2">' +
    '<!--When the bass drops, so do my problems.-->' +
    '<div class="post-files">' +
    '<div class="file_left post_file post_image post_file_left animated-bg">' +
    '<!--<img src="https://images.unsplash.com/photo-1508179719682-dbc62681c355?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2378&q=80" alt="" class="post-file_left" />-->' +
    '</div>' +
    '<div class="file_right post-right post_file_right post_image animated-bg">' +
    '<!--<img src="https://images.unsplash.com/photo-1502872364588-894d7d6ddfab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80" alt="" class="post-file" />-->' +
    '</div>' +
    '</div>' +
    '</div>' +
    actions +
    '</div>' + comment
    ;
var temp3 =
    '<!--Template 3--> ' +
    head +
    '<div class="post-content temp4">' +
    '<!--When the bass drops, so do my problems.-->' +
    '<div class="post-files">' +
    '<div class="file_left post_file post_file_left">' +
    '<div class="file-left post_image file_left_up animated-bg"><!--<img src="https://images.unsplash.com/photo-1502872364588-894d7d6ddfab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80" alt="" class="post-file" />--></div>' +
    '<div class="file-left post_image file_left_down animated-bg"><!--<img src="https://images.unsplash.com/photo-1566737236500-c8ac43014a67?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80" alt="" class="post-file" />--></div>' +
    '</div>' +
    '<div class="post-right">' +
    '<div class="file-right post_image file_right_up animated-bg"><!--<img src="https://images.unsplash.com/photo-1502872364588-894d7d6ddfab?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=2250&q=80" alt="" class="post-file" />--></div>' +
    '<div class="file-right post_image file_right_down animated-bg"><!--<img src="https://images.unsplash.com/photo-1566737236500-c8ac43014a67?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1950&q=80" alt="" class="post-file" />--></div>' +
    '</div>' +
    '</div>' +
    '</div>' +
    actions +
    '</div>' + comment
    ;


var searchBox = '<a href="" class="search-box"><div class="search-box-img"><img class="search-img" src="" /></div><div class="search-box-right"><div class="search-top">tarex_13</div><div class="search-middle">Tara Emmanuel</div></div></a>';

var sideContact = '<div class="user" onclick="contactsUrl(this)"><img src="" class="user-img" /><div class="username"><label></label><div class="user-status offline"></div></div><input class="room" value="" type="hidden"/></div > '




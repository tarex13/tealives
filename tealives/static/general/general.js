// JavaScript source code
var loading = document.createElement("div");
var loading_sub = document.createElement("div");
loading.classList.add("loading");
loading_sub.classList.add("logo");
loading_sub.innerHTML = "Tealives";
loading_sub.style = "font-size: 18vh;background: #0664d3;height: fit-content;cursor: pointer;padding: 4vh 2vh;";
loading.appendChild(loading_sub);
loading.style = "width: 100%;position: absolute;height: 100%;left: 50%;transform: translate(-50%);display: flex;align-items: center;justify-content: center;background: rgba(21, 23, 40, 1) 0%;";
document.querySelector("body").appendChild(loading);

function pLoad(container) {
    document.querySelector("." + container).style.display = "flex";
    document.querySelector("body").removeChild(document.querySelector(".loading"));
}


        // //see nice.html for some context
        // function getData(data, method, ...args) {
        //     var cloned;
        //     for (var i = 0; i < data.length; i++) {

        //         cloned = method(data[i], ...args);
        //     }
        //     if (data.length == 0) {
        //         method(false);
        //     }
        // }

        
        // /**
        //  * This function send and receives data from db
        //  * url is the url for the xhttp
        //  * params are the parameters if any
        //  * method is the method which the ready data goes thru
        //  * passMethod is any extra method that needs to be passed along
        //  * */

        // function openXmlRequest(url, requestMethod, params, method, passMethod, ...args) {
        //     //console.log("hey");
            
        //     requestMethod = requestMethod.toUpperCase();
        //     const xhttp = new XMLHttpRequest();

        //     xhttp.onreadystatechange = function () {
        //         if (this.readyState == 4 && this.status == 200) {
        //             try {
        //                 method(JSON.parse(this.responseText), passMethod, args);
        //                 //console.log("hi");
        //             } catch (e) {
        //                 console.error(e.message);
        //                 //display an error
        //             }

        //         }

        //     };
        //     xhttp.open(requestMethod, encodeURI(location.origin + "/" + url +"/"+ params));
        //     if (requestMethod == "POST") {
        //     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
        //         //Send the proper header information along with the request
        //         xhttp.setRequestHeader('X-CSRFToken', csrftoken, 'Content-type', 'application/x-www-form-urlencoded');
        //     }
        //     xhttp.send()

        // }

        //         /**
        //  * This function takes the post data and writes it into the html file
        //  **/
        //         function defaultDataTemp(data) {
        //             var prof_pic = document.querySelectorAll('.prof-pic-cont');
        //             var date = document.querySelectorAll('.post-date');
        //             var post_username = document.querySelectorAll('.post_detail_tab strong');
        //             var post_top_text = document.querySelectorAll('.post_detail_tab span');
        //             var post_content = document.querySelectorAll('.post-content');
        //             var post_actions = document.querySelectorAll('.post-actions');
        //             var textNode = document.createTextNode(data.top_text);
        //             var likes = document.querySelectorAll(".post-likes");
        //             var comments = document.querySelectorAll(".post-comments");
        
        //             prof_pic[prof_pic.length - 1].innerHTML =
        //                 '<img src="' + data.dp + '" class="prof-pic" alt="" />';
        //             post_username[post_username.length - 1].innerHTML = "@" + data.username__username;
        
        //             post_top_text[post_top_text.length - 1].innerHTML = data.title;
        //             post_content[post_content.length - 1].insertBefore(textNode, post_content[post_content.length - 1].children[0]);
        //             date[date.length - 1].innerHTML = '6 hours agos';
        //             post_content[post_content.length - 1].id = data.p_id;
        //             likes[likes.length - 1].innerHTML = data.likes;
        //             if (data.isLiked) {
        //                 post_actions[post_actions.length - 1].querySelectorAll('.post-action')[0].classList.add("active");
        //             }
        //             comments[comments.length - 1].innerHTML = data.comments;
        //             animated_bgs.forEach((bg) => bg.classList.remove('animated-bg'))
        //             animated_bg_texts.forEach((bg) => bg.classList.remove('animated-bg-text'))
        //         }
        
        
        
        //         function outputDataTemp3(data) {
        //             var file_left = document.querySelectorAll('.file_left_up');
        //             var file_right_up = document.querySelectorAll('.file_right_up');
        //             var file_right_down = document.querySelectorAll('.file_right_down');
        
        //             file_left[file_left.length - 1].innerHTML =
        //                 '<img src="' + data.files[1] + '" class="post-file" alt="" />';
        //             file_right_up[file_right_up.length - 1].innerHTML =
        //                 '<img src="' + data.files[2] + '" class="post-file" alt="" />';
        //             file_right_down[file_right_down.length - 1].innerHTML =
        //                 '<img src="' + data.files[3] + '" class="post-file" alt="" />';
        
        //         }
        
        //         function outputDataTemp4(data) {
        //             var file_left_up = document.querySelectorAll('.file_left_up');
        //             var file_left_down = document.querySelectorAll('.file_left_down');
        //             var file_right_up = document.querySelectorAll('.file_right_up');
        //             var file_right_down = document.querySelectorAll('.file_right_down');
        
        //             file_left_up[file_left_up.length - 1].innerHTML =
        //                 '<img src="' + data.files[1] + '" class="post-file" alt="" />';
        //             file_left_down[file_left_down.length - 1].innerHTML =
        //                     '<img src="' + data.files[2] + '" class="post-file" alt="" />';
        //             file_right_up[file_right_up.length - 1].innerHTML =
        //                 '<img src="' + data.files[3] + '" class="post-file" alt="" />';
        //             file_right_down[file_right_down.length - 1].innerHTML =
        //                 '<img src="' + data.files[4] + '" class="post-file" alt="" />';
        
        //         }
        
        //         function outputDataTemp2(data) {
        
        //             var file_left = document.querySelectorAll('.file_left_up');
        //             var file_right = document.querySelectorAll('.file_right_up');
        
        //             file_left[file_left.length - 1].innerHTML =
        //                 '<img src="' + data.files[1] + '" class="post-file" alt="" />';
        //             file_right[file_right.length - 1].innerHTML =
        //                 '<img src="' + data.files[2] + '" class="post-file" alt="" />';
        //         }
        //         function outputDataTemp1(data) {
        
        //             var file_left = document.querySelectorAll('.post_file_left');
        
        //             file_left[file_left.length - 1].innerHTML =
        //                 '<img src="http:\/\/127.0.0.1:8000\/media\/' + data.files__uploadedFile + '" class="post-file" alt="" />';
        //         }

                const clone = (el) => el.content.cloneNode(true);

        //         // Use this to add a new post through the temp html file created
        // function clonePost(data) {
        //     //var clonedPost = document.querySelector(".post").cloneNode(true);
        //     var postContainer = document.querySelector(".timeline-right");
        //     //postContainer.appendChild(clonedPost);
        //     // Get template from db

        //     console.log(data.template);
        //     switch (data.template) {
        //         case 1:
        //             postContainer.appendChild(clone(postTemp));
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(clone(temp1));
        //             defaultDataTemp(data);
        //             outputDataTemp1(data);
        //             break;
        //         case 2:
        //             postContainer.appendChild(clone(postTemp));
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(clone(temp2));
        //             defaultDataTemp(data);
        //             outputDataTemp2(data);
        //             break;
        //         case 3:
        //             postContainer.appendChild(clone(postTemp));
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(clone(temp3));
        //             defaultDataTemp(data);
        //             outputDataTemp3(data);
        //             break;
                    
        //         case 4:
        //             postContainer.appendChild(clone(postTemp));
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(clone(temp4));
        //             console.log(postContainer);
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(temp4);
        //             defaultDataTemp(data);
        //             outputDataTemp4(data);
        //             break;
        //         default:
        //             postContainer.appendChild(clone(postTemp));
        //             postContainer.querySelectorAll('.post-files')[post_len].appendChild(clone(temp3));
        //             defaultDataTemp(data);
        //             outputDataTemp3(data);
        //     }
            
        //     post_len++;
        // }

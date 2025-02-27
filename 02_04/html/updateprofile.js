"use strict";

function submit(){
    let fname = document.getElementById("name").value;
    let dob = document.getElementById("birthdate").value;
    let picfiles = document.getElementById("profilepic").files;
    
    if( picfiles.length === 0 ){
        alert("An error occurred! Please try again.");
        return;
    }
    fetch("/foo" );
    fetch("/foo").then( (resp) => {
        resp.text().then( (txt) => {
            console.log("Server said:",txt);
        }).catch( (err) => {
            console.log("Error getting text:",err);
        });
    }).catch( (err) => {
        console.log("Error sending request:",err);
    });
    
    let fdata = new FormData();
    fdata.append("name", name );
    fdata.append("birthday", dob );
    fdata.append("pic", picfiles[0]);
    fetch( "/do_update", {
        method: "POST",
        body: fdata
    }).then( (resp) => {
        resp.json().then( (J) => {
            console.log("Server said:",J);
        }).catch( (err) => {
            console.log("JSON error:",err);
        })
    }).catch( (err) => {
        console.log("Error:",err);
    });
}
if(document.getElementById("search") != null){
    document.querySelector("#search").addEventListener("click", search);
}

// Get the modal
var modal = document.getElementById("myModal");
// Get the <span> element that closes the modal
var spanClose = document.getElementsByClassName("close")[0];

// Get the modal image
var modalImg = document.getElementById('modal-image');
// Get the modal elements
var modalName = document.getElementById('modal-name');
var modalWeakness = document.getElementById('modal-weakness');
var modalResistance = document.getElementById('modal-strengths');
var modalImmunity = document.getElementById('modal-immunity');
var modalTypeOne = document.getElementById('modal-type-one');
var modalTypeTwo = document.getElementById('modal-type-two');
var modalWikiLink = document.getElementById('modal-wiki-link');
var modalAddToTeam = document.getElementById('modal-add');
var modalRemoveFromTeam = document.getElementById('modal-remove')

var userTeam = {};
var teamSlot = [undefined, undefined, undefined, undefined, undefined];

// When the user clicks on the + button, add Pokemon to team
function add_to_team(data) {
    for (let i = 0; i < teamSlot.length; i++) {
        if (i == 4 && teamSlot[i] != undefined) {
            alert("Team is full!")
        }

        if (teamSlot[i] == undefined) {
            data = data.split(",");
            teamSlot[i] = data[0];
            userTeam[i] = data;
            
            var pokemonElement = document.getElementById(`box-${i}`);
            pokemonElement.src = data[5]
            pokemonElement.setAttribute("title", data[1]);
            pokemonElement.setAttribute('onclick', 'click_on_sprite(\'' + data+'\')')
            modal.style.display = "none";
            break;
        }
    }
}

function remove_from_team(index) {
    var pokemonElement = document.getElementById(`box-${index}`);
    pokemonElement.src = "data:image/gif;base64,R0lGODlhAQABAAD/ACwAAAAAAQABAAACADs=";
    pokemonElement.removeAttribute('onclick');
    teamSlot[index] = "";
    delete teamSlot[index];
    modal.style.display = "none";
}

// When the user clicks on <span> (x), close the modal
spanClose.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

// When the user clicks on a sprite, open the modal
function click_on_sprite(data) {
    data = data.split(",");
    modalImg.src = data[5];
    modalImg.setAttribute('title', data[1]);

    modalName.innerHTML = "Name: " + data[1];
    modalTypeOne.innerHTML = "Type 1: " + data[3];

    if (data[4] == "") {
        modalTypeTwo.style.display = 'none';
    } else {
        modalTypeTwo.style.display = 'block';
    }

    modalTypeTwo.innerHTML = "Type 2: " + data[4];
    modalWikiLink.innerHTML = "<a href='"+data[2]+"'>Link to wiki</a>" ;

    var weaknesses = data[6].replaceAll(":", ", ");
    modalWeakness.innerHTML = "Weak against: " + weaknesses;

    var resistances = data[7].replaceAll(":", ", ");
    modalResistance.innerHTML = "Strong against: " + resistances

    var immunity = data[8].split(":");
    var immunityText = "";

    if (immunity.length == 1) {
        immunityText = immunity[0];
    }

    if (immunity.length == 2) {
        if (immunity[0] == "N/A" && immunity[1] == "N/A") {
            immunityText = "N/A";
        } else if (immunity[0] == "N/A" && immunity[1] != "N/A") {
            immunityText = immunity[1];
        } else {
            immunityText = immunity[0];
        }
    }

    if (immunity.length > 2) {
        if (immunity[0] == "N/A") {
            immunityText = immunity.slice(1, immunity.length).join(", ");
        }
        if (immunity[immunity.length-1] == "N/A") {
            immunityText = immunity.slice(0, immunity.length-1).join(", ");
        }
    }
    
    modalImmunity.innerHTML = "Immune against: " + immunityText;
    modalAddToTeam.setAttribute('onclick', 'add_to_team(\'' + data + '\')');

    var isInTeam = false;
    var slotIndex = 0;

    for (let i = 0; i < teamSlot.length; i++) {
        if (teamSlot[i] == data[0]) {
            isInTeam = true;
            slotIndex = i;
            break;
        }
    }

    if (isInTeam) {
        modalRemoveFromTeam.style.display = "block";
        modalRemoveFromTeam.setAttribute('onclick', 'remove_from_team(\'' + slotIndex + '\')');
    } else {
        modalRemoveFromTeam.style.display = "none";
    }

    modal.style.display = "block";
}

function search(){  
    debugger
    let name = document.getElementsByClassName("search_input")[0].value;
    document.querySelector(".output_space").innerHTML = "";
    $.ajax({
        url:"/process",
        type: "POST",
        data:{name: name},
    
        error: function() {
          alert('Error');
        },

        success: function(data, status, xhr) {
            debugger

            for (let i = 0; i < data.length; i++) {

                var img = document.createElement('img');
                img.src = data[i][5];
                img.setAttribute('height', '70px');
                img.setAttribute('width', '70px');
                img.setAttribute('class', 'pokeImage');
                img.setAttribute('title', data[i][1]);
                img.setAttribute('id', data[i][0]);
                img.setAttribute('onclick', 'click_on_sprite(\'' + data[i]+'\')')
                document.getElementById('outputspace').appendChild(img);
                
            }
            
          

      }})
}
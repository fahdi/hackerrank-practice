
//Setup
var contacts = [
    {
        "firstName": "Akira",
        "lastName": "Laine",
        "number": "0543236543",
        "likes": ["Pizza", "Coding", "Brownie Points"]
    },
    {
        "firstName": "Harry",
  
        "number": "0994372684",
        "likes": ["Hogwarts", "Magic", "Hagrid"]
    },
    {
        "firstName": "Sherlock",
        "lastName": "Holmes",
        "number": "0487345643",
        "likes": ["Intriguing Cases", "Violin"]
    },
    {
        "firstName": "Kristian",
        "lastName": "Vos",
        "number": "unknown",
        "likes": ["Javascript", "Gaming", "Foxes"]
    }
];


function lookUpProfile(firstName, prop){
// Only change code below this line
  var result = contacts.filter((contact) => {
    return contact.firstName == firstName;
  });  
  
  if(result.length === 0) {
    return "No such contact";
  } else {
      return result[0][prop] ? result[0][prop] : "No such property";    
  }
     
// Only change code above this line
}

// Change these values to test your function
console.log(lookUpProfile("Akira", "likes"));

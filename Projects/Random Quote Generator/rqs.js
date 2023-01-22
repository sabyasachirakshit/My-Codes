let quotes_array = [
  "Before you marry a person, you should first make them use a computer with slow Internet to see who they really are",
  "I love being married. It's so great to find that one special person you want to annoy for the rest of your life",
  "I want my children to have all the things I couldn't afford. Then I want to move in with them.",
  "Never follow anyone else’s path. Unless you’re in the woods and you’re lost and you see a path. Then by all means follow that path",
  "Insomnia sharpens your math skills because you spend all night calculating how much sleep you’ll get if you’re able to ‘fall asleep right now",
  "I haven't spoken to my wife in years. I didn't want to interrupt her.",
  "Truth hurts. Maybe not as much as jumping on a bicycle with a seat missing, but it hurts.",
  "I never feel more alone than when I’m trying to put sunscreen on my back",
  "Common sense is like deodorant. The people who need it most never use it",
  "As you get older, three things happen. The first is your memory goes, and I can’t remember the other two.",
  "I never forget a face—but in your case, I’ll be glad to make an exception.",
];

function generate() {
  let index = Math.floor(Math.random() * quotes_array.length); // random index
  document.getElementById("quotes-screen").value = quotes_array[index];
}

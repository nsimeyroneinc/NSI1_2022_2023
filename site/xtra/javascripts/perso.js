
function toAdmonitionClassString(array) {
    var s = "";
    array.forEach(element => {
      s += ".admonition."+element.toLowerCase()+", ";
      s += "details."+element.toLowerCase()+", ";
    });
    return s.substring(0,s.length-2).trim();
  }
  
  var exRendering = ["Q", "Quest", "Question"];
  var admonitionQuest = toAdmonitionClassString(questRendering);
  var quest = document.querySelectorAll(admonitionQuest);
  var nbQuest = quest.length;
  for (let i = 0; i < nbQuest; i++) {
  if (questRendering.includes(quest[i].firstElementChild.innerHTML)) {
      quest[i].firstElementChild.innerHTML = replaceBy["question"]+(i+1)+".";
  } else {
      quest[i].firstElementChild.innerHTML = replaceBy["question"]+(i+1)+". "+ex[i].firstElementChild.innerHTML
  }
  }
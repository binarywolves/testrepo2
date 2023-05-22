// Függvény a kód végrehajtásához a megfelelő oldalakon
function executeCode(pageNumber) {
  if (pageNumber === "1/4 oldal") {
    let radBtnDefault100 = document.getElementById('q0,8');
    let radBtnDefault101 = document.getElementById('q1,9');
    let radBtnDefault102 = document.getElementById('q2,9');
    let radBtnDefault103 = document.getElementById('q3,9');
    let radBtnDefault104 = document.getElementById('q4,9');
    let radBtnDefault105 = document.getElementById('q5,9');
    let radBtnDefault106 = document.getElementById('q6,9');

    radBtnDefault100.checked = true;
    radBtnDefault101.checked = true;
    radBtnDefault102.checked = true;
    radBtnDefault103.checked = true;
    radBtnDefault104.checked = true;
    radBtnDefault105.checked = true;
    radBtnDefault106.checked = true;

    let anchors100 = document.getElementsByClassName("tmsButtonRight")
    for (let i = 0; i < anchors100.length; i++) {
      if (anchors100[i].textContent == "Következő oldal") {
        anchors100[i].click();
        break;
      }
    }
  } else if (pageNumber === "2/4 oldal") {
    let radBtnDefault200 = document.getElementById('q0,8');
    let radBtnDefault201 = document.getElementById('q1,1');
    let radBtnDefault202 = document.getElementById('q2,9');
    let radBtnDefault203 = document.getElementById('q3,1');
    radBtnDefault200.checked = true;
    radBtnDefault201.checked = true;
    radBtnDefault202.checked = true;
    radBtnDefault203.checked = true;

    let anchors200 = document.getElementsByClassName("tmsButtonRight")
    for (let i = 0; i < anchors200.length; i++) {
      if (anchors200[i].textContent == "Következő oldal") {
        anchors200[i].click();
        break;
      }
    }
  } else if (pageNumber === "3/4 oldal") {
    let radBtnDefault300 = document.getElementById('q0,8');
    let radBtnDefault301 = document.getElementById('q1,2');
    radBtnDefault300.checked = true;
    radBtnDefault301.checked = true;

    let anchors300 = document.getElementsByClassName("tmsButtonRight")
    for (let i = 0; i < anchors300.length; i++) {
      if (anchors300[i].textContent == "Következő oldal") {
        anchors300[i].click();
        break;
      }
    }
  } else if (pageNumber === "4/4 oldal") {
    document.getElementById('q0,0').value = "n.a.";
    document.getElementById('q1,0').value = "n.a.";

    let anchors400 = document.getElementsByClassName("tmsButtonRight")
    for (let i = 0; i < anchors400.length; i++) {
      if (anchors400[i].textContent == "Küldés") {
        anchors400[i].click();
        break;
      }
    }
  }
}
"Küldés") {
anchors400[i].click();
break;
}
}
}
}

// Megfigyelő létrehozása a "pageNumber" div változásainak figyelésére
const observer = new MutationObserver((mutationsList) => {
  for (let mutation of mutationsList) {
    if (mutation.type === 'childList' && mutation.target.classList.contains('pageNumber')) {
      const pageNumber = mutation.target.textContent.trim();
      executeCode(pageNumber);
      break;
    }
  }
});

// Figyelés elindítása a gyökérelemre
observer.observe(document.documentElement, {
  childList: true,
  subtree: true,
});

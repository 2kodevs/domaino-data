function refresh_charts(){
  setTimeout(function start (){
    
    $('.bar').each(function(i){  
      var $bar = $(this);
      $(this).append('<span class="count"></span>')
      setTimeout(function(){
        var x = (parseInt($bar.attr('data-percent')) * 9) / 10; 
        $bar.css('width', x + '%');      
      }, i*100);
    });

    $('.count').each(function () {
        $(this).prop('Counter',0).animate({
            Counter: $(this).parent('.bar').attr('data-percent')
        }, {
            duration: 2000,
            easing: 'swing',
            step: function (now) {
                $(this).text(Math.ceil(now) +'%');
            }
        });
    });

  }, 500);
};

function new_bar(parity, label, percent){
  var cls = ['label', 'label second'];
  return `<div class="bar" data-percent="${percent}%"><span class="${cls[parity]}">${label}</span></div>\n`
};

function load(json, id){
  //TODO: get the json and remove the function argument
  json = json_data(json, id);
  var label = document.getElementById(`id${id}`).value;
  document.getElementById('main-label').innerHTML = label;
  var data = json[label];

  var p = 0;
  var lines = "";
  for(var key in data){
    if(key !== label){
      lines += new_bar(p, key, data[key]);
      p = 1 - p;
    }
  }
  document.getElementById('holder').innerHTML = lines;
  refresh_charts();
};

function json_data(json, k){
  for(var i = 1; i < k; i++){
    json = json[document.getElementById(`id${i}`).value];
  }
  return json
}

function upd_data(json, i, j){
  for(var id = i; id <= j; id++){
    populate_select(json_data(json, id), id);
  }
  load(json, j);
}

function populate_select(json, i){
  //TODO: get the json and remove the function argument
  var sel = document.getElementById(`id${i}`);
  var old_value = sel.value;
  lines = "";
  for(var key in json){
    lines += `<option value="${key}">${key}</option>\n`;
  }
  sel.innerHTML = lines;
  var new_value = sel.value;
  sel.value = old_value;
  if(sel.value === "")
    sel.value = new_value;
};

function populate_selectors(n){
  //TODO: get the json and remove the function argument
  var div = document.getElementById('selectors');
  lines = "";
  for(var i = 1; i < n; i++){
    lines += `<select name='id${i}' id='id${i}' onchange="upd_data(SITE_JSON, ${i + 1}, ${n});"></select>\n`;
  }
  lines += `<select name='id${n}' id='id${n}' onchange="load(SITE_JSON, ${n});"></select>\n`;
  div.innerHTML = lines;
};

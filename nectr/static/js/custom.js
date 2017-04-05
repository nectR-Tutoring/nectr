(function($) {

  "use strict";

  var searchBar = $("#searchbar");

  //handle search keydown
  searchBar.keypress(function (e) {
    var key = e.which;
    if(key == 13)  // the enter key code
    {
      this.value = searchBar.val();

      alert('search bar value: ' + this.value);

    }
});


})(jQuery);

var password="fach33";
var username="yaokai3a";
var guess;
var userguess=prompt('Enter Username','');
guess=prompt('Enter Password','');
if(password==guess)
alert('Success!');
else
{
  alert('Password incorrect.');
  window.location="/";
}

let checkboxes = document.querySelectorAll("input[type = 'checkbox']");
const checkAll = (myCheckBox)=>{
  let chkd = myCheckBox.checked;
  checkboxes.forEach((checkboxe)=>{
    checkboxe.checked = chkd;
  });
};


// //Qualification Table
//     // JavaScript for adding and deleting rows dynamically
//     document.addEventListener('DOMContentLoaded', function () {
//         // Add row button
//         const addRowBtn2E = document.getElementById('addRowBtn2E');
//         addRowBtn2E.addEventListener('click', function () {
//             addRow2E();
//         });

//         // Delete row buttons
//         const deleteRowBtns2E = document.querySelectorAll('.deleteRowBtn2E');
//         deleteRowBtns2E.forEach(btn => {
//             btn.addEventListener('click', function () {
//                 deleteRow2E(this);
//             });
//         });
//     });

//     // Function to add a new row
//     function addRow2E() {
//         const table = document.getElementById('qualificationTable');
//         const newRow2E = table.insertRow(table.rows.length - 1); // Insert before the last row (excluding the last row for buttons)

//         // Add cells to the new row
//         newRow2E.innerHTML = `
//             <td><input type="text" name="qualification_degree[]" class="qualification_degree"></td>
//             <td><input type="text" name="qualification_institute[]" class="qualification_institute"></td>
//             <td><input type="text" name="qualification_branch[]" class="qualification_branch"></td>
//             <td><input type="date" name="qualification_year_of_joining[]" class="qualification_year_of_joining"></td>
//             <td><input type="date" name="qualification_year_of_completion[]" class="qualification_year_of_completion"></td>
//             <td><input type="number" name="qualification_duration[]" class="qualification_duration"></td>
//             <td><input type="text" name="qualification_percentage[]" class="qualification_percentage"></td>
//             <td><input type="text" name="qualification_division[]" class="qualification_division"></td>
//             <td><button type="button" class="deleteRowBtn2E">Delete</button></td>
//         `;

//         // Attach event listener to the delete button
//         const deleteBtn2E = newRow2E.querySelector('.deleteRowBtn2E');
//         deleteBtn2E.addEventListener('click', function () {
//             deleteRow2E(this);
//         });
//     }

//     // Function to delete a row
//     function deleteRow2E(btn) {
//         const row = btn.parentNode.parentNode; // Get the parent row of the button
//         row.parentNode.removeChild(row); // Remove the row
//     }
 
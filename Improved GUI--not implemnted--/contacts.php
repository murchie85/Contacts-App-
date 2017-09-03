 <?php include ('core/init.php'); ?>


 <?php
 //create DB OBJECT 
$db = new Database;

// run query
$db->query("SELECT ALL FROM `contacts`");

// assign result set 
// contacts variable is an array with all our contacts
$contacts = $db->resultset();

?>
  <!-- DISPLAYED CONTACTS -->
        <div class="row">
        <div class="large-12 columns">
            <table>
                <thead>
                    <tr>
                        <th width="200"> Name</th>
                        <th width="130"> Phone</th>
                        <th width="200"> Email</th>
                        <th width="200"> Mobile</th>
                        <th width="200"> sex</th>
                        <th width="200"> Actions</th>
                    </tr>
                </thead>

                    <tbody>
                      <?php foreach($contacts as $contact) : ?>
                      <tr>
                          <td><a href="contact.html"> <?php echo $contact->first_name.' '.$contact->last_name; ?></a></td>
                          <td>01382675427</td>
                          <td>john@hello.com</td>
                          <td>0989896876</td>
                          <td>male</td>
                          <td>
                                <ul class ="button-group radius">
                                    <li><a href="#" class="button small">Edit</a></li>
                                    <li><a href="#" class="button small alert">Delete</a></li>
                                </ul>
                          </td>
                      </tr>
                      <?php endforeach; ?>
                    </tbody>

            </table>
            </div>
            </div>
    
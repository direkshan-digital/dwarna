<?php

/**
 * Provide an area where biobankers can edit the plugin's settings.
 * These include the configuration that is necessary to connect with the server.
 *
 * @link       https://github.com/nmamo
 * @since      1.0.0
 *
 * @package    Biobank
 * @subpackage Biobank/admin/partials
 */

require_once(plugin_dir_path(__FILE__) . "../ui/buttons.php");
require_once(plugin_dir_path(__FILE__) . "../ui/notices.php");

?>

<div class="wrap">
    <h1><?php echo esc_html( get_admin_page_title() ); ?></h1>

	<?php
		if (isset($_GET["biobank_error"]) && ! empty($_GET["biobank_error"])) {
		    echo create_error_notice($_GET["biobank_error"]);
		} else if (isset($_GET["biobank_error"]) && isset($_GET["redirect"])) {
		    echo create_success_notice("Email " . $notices[$_GET["redirect"]]);
		}
		$_GET["biobank_error"] = "";
	?>

	<h2 class="title">Email</h2>

    <form class="<?= $this->plugin_name ?>-form" id="<?= $this->plugin_name ?>-email-form" method="post" name="email_form" action=<?php echo esc_url(admin_url("admin-post.php")); ?>>
		<?php wp_nonce_field("email_form", "email_nonce"); ?>
		<input type="hidden" name="action" value="<?= $action ?>_email">
		<input type="hidden" name="<?= $this->plugin_name; ?>[email_id]" value="<?= $action != 'create' ? $email->data->id : '' ?>">

		<table class="form-table">

			<tr class="form-field">
				<th scope="row">
					<label>Recipient Group</label>
				</th>
				<td>
					<div class='radio-input-group'>
						<input name="<?= $this->plugin_name; ?>[recipient-group]"
							   type="radio" id="recipient-group-none" aria-required="true"
							   value="none" checked <?= $action == 'create' ? '' : 'disabled' ?>>
						<label for="recipient-group-none">No one</label>
					</div>

					<div class='radio-input-group'>
						<input name="<?= $this->plugin_name; ?>[recipient-group]"
							   type="radio" id="recipient-group-all" aria-required="true"
							   value="subscribed" <?= $action == 'create' ? '' : 'disabled' ?>>
						<label for="recipient-group-all">Subscribed research partners</label>
					</div>
				</td>
			</tr>

			<tr class="form-field">
				<th scope="row">
					<label for="<?= $this->plugin_name; ?>-recipient">Recipient</label>
				</th>
				<td>
					<input autocapitalize="none" autocomplete="off" autocorrect="off"
						   autofill="false" maxlength="60" name="<?= $this->plugin_name; ?>[recipient]"
						   type="text" id="<?= $this->plugin_name; ?>-recipient" aria-required="true"
						   <?= $action == 'create' ? '' : 'disabled' ?>>
				</td>
			</tr>

			<tr class="form-field" hidden>
				<th scope="row"></th>
				<td id='biobank-recipients'>
				</td>
			</tr>

			<tr class="form-field">
				<th scope="row">
					<label for="<?= $this->plugin_name; ?>-subject">Subject</label>
				</th>
				<td>
					<input autocapitalize="none" autocomplete="off" autocorrect="off"
						   autofill="false" maxlength="60" name="<?= $this->plugin_name; ?>[subject]"
						   type="text" id="<?= $this->plugin_name; ?>-subject" aria-required="true"
						   value='<?= isset($email) ? $email->data->subject : '' ?>'
						   <?= $action == 'create' ? '' : 'disabled' ?>>
				</td>
			</tr>

			<tr class="form-field">
				<th scope="row">
					<label for="<?= $this->plugin_name; ?>-body">Body</label>
				</th>
				<td>
					<input name="<?= $this->plugin_name; ?>[body]"
						   type="hidden" id="<?= $this->plugin_name; ?>-body-input" aria-required="true">
					<input name="<?= $this->plugin_name ?>[edit]"
						   type='hidden' id="<?= $this->plugin_name; ?>-edit" aria-required="true"
						   value='<?= isset($email) ? true : false ?>'>
					<?php
						$settings = array(
							'textarea_rows' => 5,
							'media_buttons' => true
						);
						wp_editor( isset($email) ? $email->data->body : '', "{$this->plugin_name}-body", $settings);
					?>
				</td>
			</tr>

		</table>

		<?php submit_button($button_labels[$action] . " email", $button_types[$action], "submit", TRUE); ?>
    </form>

	<div class="biobank-side">
		<table class="wp-list-table widefat">
			<thead>
				<th scope="col" id="name" class="manage-column column-name column-primary">Existing Emails</th>
				<th scope="col" id="name" class="manage-column column-name column-primary"></th>
			</thead>
			<tbody>
			<?php foreach ($emails as $email) { ?>
				<tr>
					<th scope="row"><?= $email->subject ?></th>
					<td><a href="<?= $admin_page ?>&action=remove&id=<?= $email->id ?>">Remove</a></td>
				</tr>
			<?php } ?>
			</tbody>
			<tfoot>
				<th scope="col" id="name" class="manage-column column-name column-primary">Existing Emails</th>
				<th scope="col" id="name" class="manage-column column-name column-primary"></th>
			</tfoot>
		</table>

		<div class="biobank-footer">
			<div class="<?= $this->plugin_name ?>-float-left"><?= strlen($pagination) > 0 ? "Pages: " . $pagination : "" ?></div>
			<form class="<?= $this->plugin_name ?>-simple-form <?= $this->plugin_name ?>-float-right" id="search_form" method="get" name="search_form" action="<?= admin_url($admin_page) ?>">
				<input name="page" type="hidden" value="<?= $plugin_page ?>" />
				<input autocapitalize="none" autocomplete="off" autocorrect="off" autofill="false" maxlength="60" name="search" placeholder="Search existing emails..." type="text" value="" aria-required="true"> <?= submit_button("Search", "secondary", $this->plugin_name . "-search") ?>
			</form>
		</div>

	</div>

</div>

<div align="left">

[![Visit Trello](./header.png)](https://developer.atlassian.com&#x2F;cloud&#x2F;trello)

# Trello<a id="trello"></a>

This document describes the REST API of Trello as published by Trello.com.
 - <a href='https://trello.com/docs/index.html' target='_blank'>Official Documentation</a>
 - <a href='https://trello.com/docs/api' target='_blank'>The HTML pages that were scraped in order to generate this specification.</a>


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`trello.action.get_board_by_id_action`](#trelloactionget_board_by_id_action)
  * [`trello.action.get_board_by_id_action_by_field`](#trelloactionget_board_by_id_action_by_field)
  * [`trello.action.get_by_id`](#trelloactionget_by_id)
  * [`trello.action.get_by_id_action_field`](#trelloactionget_by_id_action_field)
  * [`trello.action.get_card_by_id_action`](#trelloactionget_card_by_id_action)
  * [`trello.action.get_card_by_id_action_by_field`](#trelloactionget_card_by_id_action_by_field)
  * [`trello.action.get_display_by_id_action`](#trelloactionget_display_by_id_action)
  * [`trello.action.get_entities_by_id_action`](#trelloactionget_entities_by_id_action)
  * [`trello.action.get_list_by_id_action`](#trelloactionget_list_by_id_action)
  * [`trello.action.get_list_by_id_action_by_field`](#trelloactionget_list_by_id_action_by_field)
  * [`trello.action.get_member_by_field`](#trelloactionget_member_by_field)
  * [`trello.action.get_member_by_id_action`](#trelloactionget_member_by_id_action)
  * [`trello.action.get_member_by_id_action_by_field`](#trelloactionget_member_by_id_action_by_field)
  * [`trello.action.get_member_creator_by_id_action`](#trelloactionget_member_creator_by_id_action)
  * [`trello.action.get_org_by_id_action_by_field`](#trelloactionget_org_by_id_action_by_field)
  * [`trello.action.get_organization_by_id_action`](#trelloactionget_organization_by_id_action)
  * [`trello.action.remove_by_id_action`](#trelloactionremove_by_id_action)
  * [`trello.action.update_by_id_action`](#trelloactionupdate_by_id_action)
  * [`trello.action.update_text_by_id_action`](#trelloactionupdate_text_by_id_action)
  * [`trello.batch.get_data`](#trellobatchget_data)
  * [`trello.board.add_checklists`](#trelloboardadd_checklists)
  * [`trello.board.add_labels_by_id_board`](#trelloboardadd_labels_by_id_board)
  * [`trello.board.add_power_ups_by_id_board`](#trelloboardadd_power_ups_by_id_board)
  * [`trello.board.create_board`](#trelloboardcreate_board)
  * [`trello.board.create_lists_by_id_board`](#trelloboardcreate_lists_by_id_board)
  * [`trello.board.filter_cards_by_id_board`](#trelloboardfilter_cards_by_id_board)
  * [`trello.board.generate_calendar_key_by_id`](#trelloboardgenerate_calendar_key_by_id)
  * [`trello.board.generate_email_key`](#trelloboardgenerate_email_key)
  * [`trello.board.get_board_stars_by_id`](#trelloboardget_board_stars_by_id)
  * [`trello.board.get_by_id`](#trelloboardget_by_id)
  * [`trello.board.get_by_id_field`](#trelloboardget_by_id_field)
  * [`trello.board.get_cards_by_id_board`](#trelloboardget_cards_by_id_board)
  * [`trello.board.get_cards_by_id_board_by_id_card`](#trelloboardget_cards_by_id_board_by_id_card)
  * [`trello.board.get_checklists_by_id`](#trelloboardget_checklists_by_id)
  * [`trello.board.get_deltas_by_id_board`](#trelloboardget_deltas_by_id_board)
  * [`trello.board.get_labels_by_id_board_by_id_label`](#trelloboardget_labels_by_id_board_by_id_label)
  * [`trello.board.get_lists_by_filter`](#trelloboardget_lists_by_filter)
  * [`trello.board.get_lists_by_id_board`](#trelloboardget_lists_by_id_board)
  * [`trello.board.get_members_by_filter`](#trelloboardget_members_by_filter)
  * [`trello.board.get_members_by_id_board`](#trelloboardget_members_by_id_board)
  * [`trello.board.get_members_cards_by_id_board_by_id_member`](#trelloboardget_members_cards_by_id_board_by_id_member)
  * [`trello.board.get_members_invited_by_field`](#trelloboardget_members_invited_by_field)
  * [`trello.board.get_members_invited_by_id_board`](#trelloboardget_members_invited_by_id_board)
  * [`trello.board.get_memberships_by_id_board`](#trelloboardget_memberships_by_id_board)
  * [`trello.board.get_memberships_by_id_board_by_id_membership`](#trelloboardget_memberships_by_id_board_by_id_membership)
  * [`trello.board.get_my_prefs_by_id`](#trelloboardget_my_prefs_by_id)
  * [`trello.board.get_organization_by_id`](#trelloboardget_organization_by_id)
  * [`trello.board.get_organization_by_id_board_by_field`](#trelloboardget_organization_by_id_board_by_field)
  * [`trello.board.list_actions_by_id_board`](#trelloboardlist_actions_by_id_board)
  * [`trello.board.list_labels_by_id_board`](#trelloboardlist_labels_by_id_board)
  * [`trello.board.mark_as_viewed_by_id_board`](#trelloboardmark_as_viewed_by_id_board)
  * [`trello.board.remove_member`](#trelloboardremove_member)
  * [`trello.board.remove_power_up`](#trelloboardremove_power_up)
  * [`trello.board.update_by_id`](#trelloboardupdate_by_id)
  * [`trello.board.update_closed_by_id`](#trelloboardupdate_closed_by_id)
  * [`trello.board.update_description_by_id_board`](#trelloboardupdate_description_by_id_board)
  * [`trello.board.update_label_names_blue_by_id`](#trelloboardupdate_label_names_blue_by_id)
  * [`trello.board.update_label_names_green_by_id_board_put`](#trelloboardupdate_label_names_green_by_id_board_put)
  * [`trello.board.update_label_names_orange_by_id_board`](#trelloboardupdate_label_names_orange_by_id_board)
  * [`trello.board.update_label_names_purple_by_id_board`](#trelloboardupdate_label_names_purple_by_id_board)
  * [`trello.board.update_label_names_red`](#trelloboardupdate_label_names_red)
  * [`trello.board.update_label_names_yellow_by_id_board`](#trelloboardupdate_label_names_yellow_by_id_board)
  * [`trello.board.update_members_by_id_board`](#trelloboardupdate_members_by_id_board)
  * [`trello.board.update_members_by_id_board_by_id_member`](#trelloboardupdate_members_by_id_board_by_id_member)
  * [`trello.board.update_memberships_by_id_board_by_id_membership`](#trelloboardupdate_memberships_by_id_board_by_id_membership)
  * [`trello.board.update_my_prefs_email_list_by_id_board`](#trelloboardupdate_my_prefs_email_list_by_id_board)
  * [`trello.board.update_my_prefs_email_position_by_id_board`](#trelloboardupdate_my_prefs_email_position_by_id_board)
  * [`trello.board.update_my_prefs_show_list_guide_by_id_board`](#trelloboardupdate_my_prefs_show_list_guide_by_id_board)
  * [`trello.board.update_my_prefs_show_sidebar`](#trelloboardupdate_my_prefs_show_sidebar)
  * [`trello.board.update_my_prefs_show_sidebar_actions_by_id_board`](#trelloboardupdate_my_prefs_show_sidebar_actions_by_id_board)
  * [`trello.board.update_my_prefs_show_sidebar_activity_by_id_board`](#trelloboardupdate_my_prefs_show_sidebar_activity_by_id_board)
  * [`trello.board.update_name_by_id`](#trelloboardupdate_name_by_id)
  * [`trello.board.update_organization_by_id_board`](#trelloboardupdate_organization_by_id_board)
  * [`trello.board.update_prefs_background_by_id_board`](#trelloboardupdate_prefs_background_by_id_board)
  * [`trello.board.update_prefs_calendar_feed_enabled_by_id`](#trelloboardupdate_prefs_calendar_feed_enabled_by_id)
  * [`trello.board.update_prefs_card_aging_by_id_board`](#trelloboardupdate_prefs_card_aging_by_id_board)
  * [`trello.board.update_prefs_card_covers_by_id_board`](#trelloboardupdate_prefs_card_covers_by_id_board)
  * [`trello.board.update_prefs_comments_by_id_board`](#trelloboardupdate_prefs_comments_by_id_board)
  * [`trello.board.update_prefs_invitations_by_id_board`](#trelloboardupdate_prefs_invitations_by_id_board)
  * [`trello.board.update_prefs_permission_level_by_id`](#trelloboardupdate_prefs_permission_level_by_id)
  * [`trello.board.update_prefs_self_join_by_id_board`](#trelloboardupdate_prefs_self_join_by_id_board)
  * [`trello.board.update_prefs_show_sidebar_members_by_id`](#trelloboardupdate_prefs_show_sidebar_members_by_id)
  * [`trello.board.update_subscribed_by_id`](#trelloboardupdate_subscribed_by_id)
  * [`trello.board.update_voting_prefs_by_id`](#trelloboardupdate_voting_prefs_by_id)
  * [`trello.card.add_actions_comments_by_id_card`](#trellocardadd_actions_comments_by_id_card)
  * [`trello.card.add_attachments_by_id_card`](#trellocardadd_attachments_by_id_card)
  * [`trello.card.add_checklist_check_item`](#trellocardadd_checklist_check_item)
  * [`trello.card.add_checklists`](#trellocardadd_checklists)
  * [`trello.card.add_id_labels_to_card`](#trellocardadd_id_labels_to_card)
  * [`trello.card.add_labels`](#trellocardadd_labels)
  * [`trello.card.add_members`](#trellocardadd_members)
  * [`trello.card.add_members_voted`](#trellocardadd_members_voted)
  * [`trello.card.add_stickers_by_id_card`](#trellocardadd_stickers_by_id_card)
  * [`trello.card.convert_check_item_to_card`](#trellocardconvert_check_item_to_card)
  * [`trello.card.create_and_update`](#trellocardcreate_and_update)
  * [`trello.card.delete_attachments_by_id_card_by_id_attachment`](#trellocarddelete_attachments_by_id_card_by_id_attachment)
  * [`trello.card.delete_checklist_by_id_card_by_id_checklist`](#trellocarddelete_checklist_by_id_card_by_id_checklist)
  * [`trello.card.get_attachments_by_id_card`](#trellocardget_attachments_by_id_card)
  * [`trello.card.get_attachments_by_ids`](#trellocardget_attachments_by_ids)
  * [`trello.card.get_board_by_id`](#trellocardget_board_by_id)
  * [`trello.card.get_board_by_id_card_by_field`](#trellocardget_board_by_id_card_by_field)
  * [`trello.card.get_by_id`](#trellocardget_by_id)
  * [`trello.card.get_by_id_field`](#trellocardget_by_id_field)
  * [`trello.card.get_cards_list_by_id_card_by_field`](#trellocardget_cards_list_by_id_card_by_field)
  * [`trello.card.get_check_item_states_by_id`](#trellocardget_check_item_states_by_id)
  * [`trello.card.get_checklists_by_id`](#trellocardget_checklists_by_id)
  * [`trello.card.get_list_by_id`](#trellocardget_list_by_id)
  * [`trello.card.get_members_voted_by_id_card`](#trellocardget_members_voted_by_id_card)
  * [`trello.card.get_sticker_by_ids`](#trellocardget_sticker_by_ids)
  * [`trello.card.get_stickers_by_id_card`](#trellocardget_stickers_by_id_card)
  * [`trello.card.list_card_actions_by_id`](#trellocardlist_card_actions_by_id)
  * [`trello.card.list_members_by_id_card`](#trellocardlist_members_by_id_card)
  * [`trello.card.mark_associated_notifications_read`](#trellocardmark_associated_notifications_read)
  * [`trello.card.remove_action_comment_by_id_card_by_id_action`](#trellocardremove_action_comment_by_id_card_by_id_action)
  * [`trello.card.remove_by_id_card`](#trellocardremove_by_id_card)
  * [`trello.card.remove_checklist_check_item`](#trellocardremove_checklist_check_item)
  * [`trello.card.remove_label_by_id_card_by_id_label`](#trellocardremove_label_by_id_card_by_id_label)
  * [`trello.card.remove_labels_by_id_card_by_color`](#trellocardremove_labels_by_id_card_by_color)
  * [`trello.card.remove_member_by_id_member`](#trellocardremove_member_by_id_member)
  * [`trello.card.remove_members_voted_by_id_card_by_id_member`](#trellocardremove_members_voted_by_id_card_by_id_member)
  * [`trello.card.remove_sticker_by_ids`](#trellocardremove_sticker_by_ids)
  * [`trello.card.update_action_comment_by_id_card_by_id_action`](#trellocardupdate_action_comment_by_id_card_by_id_action)
  * [`trello.card.update_attachment_cover_by_id_card`](#trellocardupdate_attachment_cover_by_id_card)
  * [`trello.card.update_board_by_id_card`](#trellocardupdate_board_by_id_card)
  * [`trello.card.update_by_id_card`](#trellocardupdate_by_id_card)
  * [`trello.card.update_check_item_pos_by_id`](#trellocardupdate_check_item_pos_by_id)
  * [`trello.card.update_checklist_check_item`](#trellocardupdate_checklist_check_item)
  * [`trello.card.update_checklist_check_item_name_by_id`](#trellocardupdate_checklist_check_item_name_by_id)
  * [`trello.card.update_checklist_check_item_state`](#trellocardupdate_checklist_check_item_state)
  * [`trello.card.update_closed_by_id`](#trellocardupdate_closed_by_id)
  * [`trello.card.update_description_by_id_card`](#trellocardupdate_description_by_id_card)
  * [`trello.card.update_due_by_id`](#trellocardupdate_due_by_id)
  * [`trello.card.update_id_list_by_id_card`](#trellocardupdate_id_list_by_id_card)
  * [`trello.card.update_id_members`](#trellocardupdate_id_members)
  * [`trello.card.update_labels`](#trellocardupdate_labels)
  * [`trello.card.update_name_by_id`](#trellocardupdate_name_by_id)
  * [`trello.card.update_pos_by_id_card`](#trellocardupdate_pos_by_id_card)
  * [`trello.card.update_stickers_by_id_card_by_id_sticker`](#trellocardupdate_stickers_by_id_card_by_id_sticker)
  * [`trello.card.update_subscribed_by_id_card`](#trellocardupdate_subscribed_by_id_card)
  * [`trello.checklist.add_check_items_by_id_checklist`](#trellochecklistadd_check_items_by_id_checklist)
  * [`trello.checklist.create`](#trellochecklistcreate)
  * [`trello.checklist.get_board_by_id_checklist`](#trellochecklistget_board_by_id_checklist)
  * [`trello.checklist.get_board_by_id_checklist_by_field`](#trellochecklistget_board_by_id_checklist_by_field)
  * [`trello.checklist.get_by_id`](#trellochecklistget_by_id)
  * [`trello.checklist.get_by_id_field`](#trellochecklistget_by_id_field)
  * [`trello.checklist.get_cards_by_filter`](#trellochecklistget_cards_by_filter)
  * [`trello.checklist.get_check_items_by_id_checklist`](#trellochecklistget_check_items_by_id_checklist)
  * [`trello.checklist.get_check_items_by_id_checklist_by_id_check_item`](#trellochecklistget_check_items_by_id_checklist_by_id_check_item)
  * [`trello.checklist.list_cards_by_id_checklist`](#trellochecklistlist_cards_by_id_checklist)
  * [`trello.checklist.remove_by_id`](#trellochecklistremove_by_id)
  * [`trello.checklist.remove_by_id_check_item`](#trellochecklistremove_by_id_check_item)
  * [`trello.checklist.update_by_id_checklist`](#trellochecklistupdate_by_id_checklist)
  * [`trello.checklist.update_id_card_by_id_checklist`](#trellochecklistupdate_id_card_by_id_checklist)
  * [`trello.checklist.update_name_by_id_checklist`](#trellochecklistupdate_name_by_id_checklist)
  * [`trello.checklist.update_pos_by_id_checklist`](#trellochecklistupdate_pos_by_id_checklist)
  * [`trello.label.create_labels`](#trellolabelcreate_labels)
  * [`trello.label.get_board_by_id_label`](#trellolabelget_board_by_id_label)
  * [`trello.label.get_board_by_id_label_by_field`](#trellolabelget_board_by_id_label_by_field)
  * [`trello.label.get_by_id_label`](#trellolabelget_by_id_label)
  * [`trello.label.remove_by_id_label`](#trellolabelremove_by_id_label)
  * [`trello.label.update_by_id_label`](#trellolabelupdate_by_id_label)
  * [`trello.label.update_color_by_id_label`](#trellolabelupdate_color_by_id_label)
  * [`trello.label.update_name_by_id_label`](#trellolabelupdate_name_by_id_label)
  * [`trello.list.archive_all_cards_by_id_list`](#trellolistarchive_all_cards_by_id_list)
  * [`trello.list.create_cards_by_id_list`](#trellolistcreate_cards_by_id_list)
  * [`trello.list.create_list`](#trellolistcreate_list)
  * [`trello.list.get_actions_by_id_list`](#trellolistget_actions_by_id_list)
  * [`trello.list.get_board_by_id_list_by_field`](#trellolistget_board_by_id_list_by_field)
  * [`trello.list.get_by_id_list`](#trellolistget_by_id_list)
  * [`trello.list.get_by_id_list_by_field`](#trellolistget_by_id_list_by_field)
  * [`trello.list.get_cards_by_filter`](#trellolistget_cards_by_filter)
  * [`trello.list.get_cards_by_id_list`](#trellolistget_cards_by_id_list)
  * [`trello.list.id_board_get`](#trellolistid_board_get)
  * [`trello.list.move_all_cards_by_id_list`](#trellolistmove_all_cards_by_id_list)
  * [`trello.list.update_by_id_list`](#trellolistupdate_by_id_list)
  * [`trello.list.update_closed_by_id_list`](#trellolistupdate_closed_by_id_list)
  * [`trello.list.update_id_board_by_id_list`](#trellolistupdate_id_board_by_id_list)
  * [`trello.list.update_name_by_id_list`](#trellolistupdate_name_by_id_list)
  * [`trello.list.update_pos_by_id_list`](#trellolistupdate_pos_by_id_list)
  * [`trello.list.update_subscribed_by_id_list`](#trellolistupdate_subscribed_by_id_list)
  * [`trello.member.add_board_backgrounds`](#trellomemberadd_board_backgrounds)
  * [`trello.member.add_board_stars_by_id_member`](#trellomemberadd_board_stars_by_id_member)
  * [`trello.member.add_custom_board_backgrounds`](#trellomemberadd_custom_board_backgrounds)
  * [`trello.member.add_custom_emoji_by_id_member`](#trellomemberadd_custom_emoji_by_id_member)
  * [`trello.member.add_custom_stickers`](#trellomemberadd_custom_stickers)
  * [`trello.member.add_one_time_messages_dismissed_by_id_member`](#trellomemberadd_one_time_messages_dismissed_by_id_member)
  * [`trello.member.create_saved_search`](#trellomembercreate_saved_search)
  * [`trello.member.delete_board_background`](#trellomemberdelete_board_background)
  * [`trello.member.get_board_background_by_ids`](#trellomemberget_board_background_by_ids)
  * [`trello.member.get_board_backgrounds_by_id`](#trellomemberget_board_backgrounds_by_id)
  * [`trello.member.get_board_star_by_id_member`](#trellomemberget_board_star_by_id_member)
  * [`trello.member.get_board_stars_by_id`](#trellomemberget_board_stars_by_id)
  * [`trello.member.get_boards`](#trellomemberget_boards)
  * [`trello.member.get_boards_by_id_member`](#trellomemberget_boards_by_id_member)
  * [`trello.member.get_boards_invited_by_id_member_by_field`](#trellomemberget_boards_invited_by_id_member_by_field)
  * [`trello.member.get_by_field`](#trellomemberget_by_field)
  * [`trello.member.get_by_id`](#trellomemberget_by_id)
  * [`trello.member.get_cards_by_filter`](#trellomemberget_cards_by_filter)
  * [`trello.member.get_cards_by_id_member`](#trellomemberget_cards_by_id_member)
  * [`trello.member.get_custom_board_background_by_ids`](#trellomemberget_custom_board_background_by_ids)
  * [`trello.member.get_custom_board_backgrounds_by_id`](#trellomemberget_custom_board_backgrounds_by_id)
  * [`trello.member.get_custom_emoji_by_ids`](#trellomemberget_custom_emoji_by_ids)
  * [`trello.member.get_custom_sticker_by_ids`](#trellomemberget_custom_sticker_by_ids)
  * [`trello.member.get_custom_stickers_by_id_member`](#trellomemberget_custom_stickers_by_id_member)
  * [`trello.member.get_deltas_by_id_member`](#trellomemberget_deltas_by_id_member)
  * [`trello.member.get_invited_boards`](#trellomemberget_invited_boards)
  * [`trello.member.get_notifications_by_id_member`](#trellomemberget_notifications_by_id_member)
  * [`trello.member.get_notifications_by_id_member_by_filter`](#trellomemberget_notifications_by_id_member_by_filter)
  * [`trello.member.get_organizations`](#trellomemberget_organizations)
  * [`trello.member.get_saved_search_by_ids`](#trellomemberget_saved_search_by_ids)
  * [`trello.member.get_saved_searches_by_id_member`](#trellomemberget_saved_searches_by_id_member)
  * [`trello.member.get_tokens_by_id_member`](#trellomemberget_tokens_by_id_member)
  * [`trello.member.list_actions_by_id_member`](#trellomemberlist_actions_by_id_member)
  * [`trello.member.list_custom_emoji_by_id_member`](#trellomemberlist_custom_emoji_by_id_member)
  * [`trello.member.list_invited_organizations_by_id`](#trellomemberlist_invited_organizations_by_id)
  * [`trello.member.list_organizations_by_id`](#trellomemberlist_organizations_by_id)
  * [`trello.member.list_organizations_invited_by_id_member_by_field`](#trellomemberlist_organizations_invited_by_id_member_by_field)
  * [`trello.member.remove_board_star_by_id_member_by_id_board_star`](#trellomemberremove_board_star_by_id_member_by_id_board_star)
  * [`trello.member.remove_custom_board_background_by_id`](#trellomemberremove_custom_board_background_by_id)
  * [`trello.member.remove_custom_sticker_by_ids`](#trellomemberremove_custom_sticker_by_ids)
  * [`trello.member.remove_saved_search_by_ids`](#trellomemberremove_saved_search_by_ids)
  * [`trello.member.update_avatar_source`](#trellomemberupdate_avatar_source)
  * [`trello.member.update_bio_by_id`](#trellomemberupdate_bio_by_id)
  * [`trello.member.update_board_backgrounds_by_id`](#trellomemberupdate_board_backgrounds_by_id)
  * [`trello.member.update_board_star`](#trellomemberupdate_board_star)
  * [`trello.member.update_board_star_pos_by_id_member_by_id_board_star`](#trellomemberupdate_board_star_pos_by_id_member_by_id_board_star)
  * [`trello.member.update_board_stars_id_board`](#trellomemberupdate_board_stars_id_board)
  * [`trello.member.update_by_id_member`](#trellomemberupdate_by_id_member)
  * [`trello.member.update_custom_board_backgrounds`](#trellomemberupdate_custom_board_backgrounds)
  * [`trello.member.update_full_name`](#trellomemberupdate_full_name)
  * [`trello.member.update_initials_by_id_member`](#trellomemberupdate_initials_by_id_member)
  * [`trello.member.update_prefs_color_blind_by_id_member`](#trellomemberupdate_prefs_color_blind_by_id_member)
  * [`trello.member.update_prefs_locale_by_id_member`](#trellomemberupdate_prefs_locale_by_id_member)
  * [`trello.member.update_prefs_minutes_between_summaries_by_id`](#trellomemberupdate_prefs_minutes_between_summaries_by_id)
  * [`trello.member.update_saved_search_query_by_id_member_by_id_saved_search`](#trellomemberupdate_saved_search_query_by_id_member_by_id_saved_search)
  * [`trello.member.update_saved_searches_by_id_member_by_id_saved_search`](#trellomemberupdate_saved_searches_by_id_member_by_id_saved_search)
  * [`trello.member.update_saved_searches_name_by_id_member_by_id_saved_search`](#trellomemberupdate_saved_searches_name_by_id_member_by_id_saved_search)
  * [`trello.member.update_saved_searches_pos_by_id_member_by_id_saved_search`](#trellomemberupdate_saved_searches_pos_by_id_member_by_id_saved_search)
  * [`trello.member.update_username_by_id`](#trellomemberupdate_username_by_id)
  * [`trello.member.upload_avatar_by_id`](#trellomemberupload_avatar_by_id)
  * [`trello.notification.get_board_by_field`](#trellonotificationget_board_by_field)
  * [`trello.notification.get_board_by_id`](#trellonotificationget_board_by_id)
  * [`trello.notification.get_by_id`](#trellonotificationget_by_id)
  * [`trello.notification.get_by_id_field`](#trellonotificationget_by_id_field)
  * [`trello.notification.get_card_by_id`](#trellonotificationget_card_by_id)
  * [`trello.notification.get_card_by_id_notification_by_field`](#trellonotificationget_card_by_id_notification_by_field)
  * [`trello.notification.get_display_by_id_notification`](#trellonotificationget_display_by_id_notification)
  * [`trello.notification.get_entities_by_id_notification`](#trellonotificationget_entities_by_id_notification)
  * [`trello.notification.get_list_by_id_notification`](#trellonotificationget_list_by_id_notification)
  * [`trello.notification.get_list_by_id_notification_by_field`](#trellonotificationget_list_by_id_notification_by_field)
  * [`trello.notification.get_member_by_id_field`](#trellonotificationget_member_by_id_field)
  * [`trello.notification.get_member_by_id_notification_by_field`](#trellonotificationget_member_by_id_notification_by_field)
  * [`trello.notification.get_member_by_notification`](#trellonotificationget_member_by_notification)
  * [`trello.notification.get_member_creator_by_id`](#trellonotificationget_member_creator_by_id)
  * [`trello.notification.get_organization_by_id_notification`](#trellonotificationget_organization_by_id_notification)
  * [`trello.notification.get_organization_by_id_notification_by_field`](#trellonotificationget_organization_by_id_notification_by_field)
  * [`trello.notification.mark_all_as_read`](#trellonotificationmark_all_as_read)
  * [`trello.notification.update_by_id_notification`](#trellonotificationupdate_by_id_notification)
  * [`trello.notification.update_unread_by_id_notification`](#trellonotificationupdate_unread_by_id_notification)
  * [`trello.organization.create`](#trelloorganizationcreate)
  * [`trello.organization.delete_prefs_associated_domain_by_id_org`](#trelloorganizationdelete_prefs_associated_domain_by_id_org)
  * [`trello.organization.get_actions_by_id_org`](#trelloorganizationget_actions_by_id_org)
  * [`trello.organization.get_boards_by_id_org_by_filter`](#trelloorganizationget_boards_by_id_org_by_filter)
  * [`trello.organization.get_boards_by_org_id`](#trelloorganizationget_boards_by_org_id)
  * [`trello.organization.get_by_id_and_field`](#trelloorganizationget_by_id_and_field)
  * [`trello.organization.get_by_id_org`](#trelloorganizationget_by_id_org)
  * [`trello.organization.get_members_by_id_org`](#trelloorganizationget_members_by_id_org)
  * [`trello.organization.get_members_invited_by_id_org`](#trelloorganizationget_members_invited_by_id_org)
  * [`trello.organization.get_members_invited_by_id_org_by_field`](#trelloorganizationget_members_invited_by_id_org_by_field)
  * [`trello.organization.get_memberships_by_id_org_by_id_membership`](#trelloorganizationget_memberships_by_id_org_by_id_membership)
  * [`trello.organization.get_organization_deltas`](#trelloorganizationget_organization_deltas)
  * [`trello.organization.list_members_by_id_org_by_filter`](#trelloorganizationlist_members_by_id_org_by_filter)
  * [`trello.organization.list_members_cards_by_id_org_by_id_member`](#trelloorganizationlist_members_cards_by_id_org_by_id_member)
  * [`trello.organization.list_memberships_by_id_org`](#trelloorganizationlist_memberships_by_id_org)
  * [`trello.organization.remove_by_id_org`](#trelloorganizationremove_by_id_org)
  * [`trello.organization.remove_invite_restrict_by_id_org`](#trelloorganizationremove_invite_restrict_by_id_org)
  * [`trello.organization.remove_logo_by_id_org`](#trelloorganizationremove_logo_by_id_org)
  * [`trello.organization.remove_member_all`](#trelloorganizationremove_member_all)
  * [`trello.organization.remove_member_by_id_org_by_id_member`](#trelloorganizationremove_member_by_id_org_by_id_member)
  * [`trello.organization.update_by_id_org`](#trelloorganizationupdate_by_id_org)
  * [`trello.organization.update_description_by_id_org`](#trelloorganizationupdate_description_by_id_org)
  * [`trello.organization.update_display_name_by_id_org`](#trelloorganizationupdate_display_name_by_id_org)
  * [`trello.organization.update_members_by_id_org`](#trelloorganizationupdate_members_by_id_org)
  * [`trello.organization.update_members_by_id_org_by_id_member`](#trelloorganizationupdate_members_by_id_org_by_id_member)
  * [`trello.organization.update_members_deactivated_by_id_org_by_id_member`](#trelloorganizationupdate_members_deactivated_by_id_org_by_id_member)
  * [`trello.organization.update_membership_by_id_org_by_id_membership`](#trelloorganizationupdate_membership_by_id_org_by_id_membership)
  * [`trello.organization.update_name_by_id_org`](#trelloorganizationupdate_name_by_id_org)
  * [`trello.organization.update_prefs_associated_domain_by_id_org`](#trelloorganizationupdate_prefs_associated_domain_by_id_org)
  * [`trello.organization.update_prefs_board_visibility_restrict_by_id_org`](#trelloorganizationupdate_prefs_board_visibility_restrict_by_id_org)
  * [`trello.organization.update_prefs_board_visibility_restrict_public_by_id_org`](#trelloorganizationupdate_prefs_board_visibility_restrict_public_by_id_org)
  * [`trello.organization.update_prefs_external_members_disabled_by_id_org`](#trelloorganizationupdate_prefs_external_members_disabled_by_id_org)
  * [`trello.organization.update_prefs_google_apps_version_by_id_org`](#trelloorganizationupdate_prefs_google_apps_version_by_id_org)
  * [`trello.organization.update_prefs_org_invite_restrict_by_id_org`](#trelloorganizationupdate_prefs_org_invite_restrict_by_id_org)
  * [`trello.organization.update_prefs_permission_level_by_id_org`](#trelloorganizationupdate_prefs_permission_level_by_id_org)
  * [`trello.organization.update_prefs_visibility_by_id_org`](#trelloorganizationupdate_prefs_visibility_by_id_org)
  * [`trello.organization.update_website_by_id_org`](#trelloorganizationupdate_website_by_id_org)
  * [`trello.organization.upload_logo_by_id_org`](#trelloorganizationupload_logo_by_id_org)
  * [`trello.search.find_members`](#trellosearchfind_members)
  * [`trello.search.get_results`](#trellosearchget_results)
  * [`trello.session.create_and_update`](#trellosessioncreate_and_update)
  * [`trello.session.get_socket_sessions`](#trellosessionget_socket_sessions)
  * [`trello.session.update_status_by_id_session`](#trellosessionupdate_status_by_id_session)
  * [`trello.session.update_status_by_id_session_0`](#trellosessionupdate_status_by_id_session_0)
  * [`trello.token.delete_by_token`](#trellotokendelete_by_token)
  * [`trello.token.get_by_token`](#trellotokenget_by_token)
  * [`trello.token.get_by_token_by_field`](#trellotokenget_by_token_by_field)
  * [`trello.token.get_member_by_field`](#trellotokenget_member_by_field)
  * [`trello.token.get_member_by_token`](#trellotokenget_member_by_token)
  * [`trello.token.get_webhook_by_id`](#trellotokenget_webhook_by_id)
  * [`trello.token.get_webhooks`](#trellotokenget_webhooks)
  * [`trello.token.register_webhook`](#trellotokenregister_webhook)
  * [`trello.token.remove_by_token_by_id_webhook`](#trellotokenremove_by_token_by_id_webhook)
  * [`trello.token.update_webhooks_by_token`](#trellotokenupdate_webhooks_by_token)
  * [`trello.type.get_by_id`](#trellotypeget_by_id)
  * [`trello.webhook.get_by_id`](#trellowebhookget_by_id)
  * [`trello.webhook.get_by_id_field`](#trellowebhookget_by_id_field)
  * [`trello.webhook.remove_by_id`](#trellowebhookremove_by_id)
  * [`trello.webhook.update`](#trellowebhookupdate)
  * [`trello.webhook.update_active_by_id`](#trellowebhookupdate_active_by_id)
  * [`trello.webhook.update_by_id_webhook`](#trellowebhookupdate_by_id_webhook)
  * [`trello.webhook.update_callback_url_by_id`](#trellowebhookupdate_callback_url_by_id)
  * [`trello.webhook.update_description_by_id_webhook`](#trellowebhookupdate_description_by_id_webhook)
  * [`trello.webhook.update_model_by_id`](#trellowebhookupdate_model_by_id)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Trello&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from trello_python_sdk import Trello, ApiException

trello = Trello(

        api_key = 'YOUR_API_KEY',

        api_token = 'YOUR_API_KEY',
)

try:
    # getActionsBoardByIdAction()
    trello.action.get_board_by_id_action(
        id_action="idAction_example",
        fields="all",
    )
except ApiException as e:
    print("Exception when calling ActionApi.get_board_by_id_action: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from trello_python_sdk import Trello, ApiException

trello = Trello(

        api_key = 'YOUR_API_KEY',

        api_token = 'YOUR_API_KEY',
)

async def main():
    try:
        # getActionsBoardByIdAction()
        await trello.action.aget_board_by_id_action(
            id_action="idAction_example",
            fields="all",
        )
    except ApiException as e:
        print("Exception when calling ActionApi.get_board_by_id_action: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from trello_python_sdk import Trello, ApiException

trello = Trello(

        api_key = 'YOUR_API_KEY',

        api_token = 'YOUR_API_KEY',
)

try:
    # getActionsBoardByIdAction()
    get_board_by_id_action_response = trello.action.raw.get_board_by_id_action(
        id_action="idAction_example",
        fields="all",
    )
    pprint(get_board_by_id_action_response.headers)
    pprint(get_board_by_id_action_response.status)
    pprint(get_board_by_id_action_response.round_trip_time)
except ApiException as e:
    print("Exception when calling ActionApi.get_board_by_id_action: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `trello.action.get_board_by_id_action`<a id="trelloactionget_board_by_id_action"></a>

getActionsBoardByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_board_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_board_by_id_action_by_field`<a id="trelloactionget_board_by_id_action_by_field"></a>

getActionsBoardByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_board_by_id_action_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_by_id`<a id="trelloactionget_by_id"></a>

getActionsByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_by_id(
    id_action="idAction_example",
    display="string_example",
    entities="string_example",
    fields="all",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### display: `str`<a id="display-str"></a>

 true or false

##### entities: `str`<a id="entities-str"></a>

 true or false

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_by_id_action_field`<a id="trelloactionget_by_id_action_field"></a>

getActionsByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_by_id_action_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_card_by_id_action`<a id="trelloactionget_card_by_id_action"></a>

getActionsCardByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_card_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/card` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_card_by_id_action_by_field`<a id="trelloactionget_card_by_id_action_by_field"></a>

getActionsCardByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_card_by_id_action_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/card/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_display_by_id_action`<a id="trelloactionget_display_by_id_action"></a>

getActionsDisplayByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_display_by_id_action(
    id_action="idAction_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/display` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_entities_by_id_action`<a id="trelloactionget_entities_by_id_action"></a>

getActionsEntitiesByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_entities_by_id_action(
    id_action="idAction_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_list_by_id_action`<a id="trelloactionget_list_by_id_action"></a>

getActionsListByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_list_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_list_by_id_action_by_field`<a id="trelloactionget_list_by_id_action_by_field"></a>

getActionsListByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_list_by_id_action_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/list/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_member_by_field`<a id="trelloactionget_member_by_field"></a>

getActionsMemberByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_member_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/member/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_member_by_id_action`<a id="trelloactionget_member_by_id_action"></a>

getActionsMemberByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_member_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/member` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_member_by_id_action_by_field`<a id="trelloactionget_member_by_id_action_by_field"></a>

getActionsMemberCreatorByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_member_by_id_action_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/memberCreator/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_member_creator_by_id_action`<a id="trelloactionget_member_creator_by_id_action"></a>

getActionsMemberCreatorByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_member_creator_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/memberCreator` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_org_by_id_action_by_field`<a id="trelloactionget_org_by_id_action_by_field"></a>

getActionsOrganizationByIdActionByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_org_by_id_action_by_field(
    id_action="idAction_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/organization/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.get_organization_by_id_action`<a id="trelloactionget_organization_by_id_action"></a>

getActionsOrganizationByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.get_organization_by_id_action(
    id_action="idAction_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/organization` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.remove_by_id_action`<a id="trelloactionremove_by_id_action"></a>

deleteActionsByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.remove_by_id_action(
    id_action="idAction_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.update_by_id_action`<a id="trelloactionupdate_by_id_action"></a>

updateActionsByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.update_by_id_action(
    id_action="idAction_example",
    text="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### text: `str`<a id="text-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Actions`](./trello_python_sdk/type/actions.py)
Attributes of \"Actions\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.action.update_text_by_id_action`<a id="trelloactionupdate_text_by_id_action"></a>

updateActionsTextByIdAction()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.action.update_text_by_id_action(
    id_action="idAction_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsText`](./trello_python_sdk/type/actions_text.py)
Attributes of \"Actions Text\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/actions/{idAction}/text` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.batch.get_data`<a id="trellobatchget_data"></a>

getBatch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.batch.get_data(
    urls="urls_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### urls: `str`<a id="urls-str"></a>

list of API v1 GET routes, not including the version prefix

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/batch` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.add_checklists`<a id="trelloboardadd_checklists"></a>

addBoardsChecklistsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.add_checklists(
    id_board="idBoard_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsChecklists`](./trello_python_sdk/type/boards_checklists.py)
Attributes of \"Boards Checklists\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/checklists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.add_labels_by_id_board`<a id="trelloboardadd_labels_by_id_board"></a>

addBoardsLabelsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.add_labels_by_id_board(
    id_board="idBoard_example",
    color="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### color: `str`<a id="color-str"></a>

A valid label color or null

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsLabels`](./trello_python_sdk/type/boards_labels.py)
Attributes of \"Boards Labels\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.add_power_ups_by_id_board`<a id="trelloboardadd_power_ups_by_id_board"></a>

addBoardsPowerUpsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.add_power_ups_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: calendar, cardAging, recap or voting

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsPowerUps`](./trello_python_sdk/type/boards_power_ups.py)
Attributes of \"Boards Power Ups\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/powerUps` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.create_board`<a id="trelloboardcreate_board"></a>

addBoards()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.create_board(
    closed="string_example",
    desc="string_example",
    id_board_source="string_example",
    id_organization="string_example",
    keep_from_source="string_example",
    label_names_blue="string_example",
    label_names_green="string_example",
    label_names_orange="string_example",
    label_names_purple="string_example",
    label_names_red="string_example",
    label_names_yellow="string_example",
    name="string_example",
    power_ups="string_example",
    prefs_background="string_example",
    prefs_calendar_feed_enabled="string_example",
    prefs_card_aging="string_example",
    prefs_card_covers="string_example",
    prefs_comments="string_example",
    prefs_invitations="string_example",
    prefs_permission_level="string_example",
    prefs_self_join="string_example",
    prefs_voting="string_example",
    prefs_background="string_example",
    prefs_card_aging="string_example",
    prefs_card_covers="string_example",
    prefs_comments="string_example",
    prefs_invitations="string_example",
    prefs_permission_level="string_example",
    prefs_self_join="string_example",
    prefs_voting="string_example",
    subscribed="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### closed: `str`<a id="closed-str"></a>

 true or false

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### id_board_source: `str`<a id="id_board_source-str"></a>

The id of the board to copy into the new board

##### id_organization: `str`<a id="id_organization-str"></a>

The id or name of the organization to add the board to.

##### keep_from_source: `str`<a id="keep_from_source-str"></a>

Components of the source board to copy.

##### label_names_blue: `str`<a id="label_names_blue-str"></a>

a string with a length from 0 to 16384

##### label_names_green: `str`<a id="label_names_green-str"></a>

a string with a length from 0 to 16384

##### label_names_orange: `str`<a id="label_names_orange-str"></a>

a string with a length from 0 to 16384

##### label_names_purple: `str`<a id="label_names_purple-str"></a>

a string with a length from 0 to 16384

##### label_names_red: `str`<a id="label_names_red-str"></a>

a string with a length from 0 to 16384

##### label_names_yellow: `str`<a id="label_names_yellow-str"></a>

a string with a length from 0 to 16384

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### power_ups: `str`<a id="power_ups-str"></a>

all or a comma-separated list of: calendar, cardAging, recap or voting

##### prefs_background: `str`<a id="prefs_background-str"></a>

A standard background name, or the id of a custom background

##### prefs_calendar_feed_enabled: `str`<a id="prefs_calendar_feed_enabled-str"></a>

 true or false

##### prefs_card_aging: `str`<a id="prefs_card_aging-str"></a>

One of: pirate or regular

##### prefs_card_covers: `str`<a id="prefs_card_covers-str"></a>

 true or false

##### prefs_comments: `str`<a id="prefs_comments-str"></a>

One of: disabled, members, observers, org or public

##### prefs_invitations: `str`<a id="prefs_invitations-str"></a>

One of: admins or members

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: org, private or public

##### prefs_self_join: `str`<a id="prefs_self_join-str"></a>

 true or false

##### prefs_voting: `str`<a id="prefs_voting-str"></a>

One of: disabled, members, observers, org or public

##### prefs_background: `str`<a id="prefs_background-str"></a>

a string with a length from 0 to 16384

##### prefs_card_aging: `str`<a id="prefs_card_aging-str"></a>

One of: pirate or regular

##### prefs_card_covers: `str`<a id="prefs_card_covers-str"></a>

 true or false

##### prefs_comments: `str`<a id="prefs_comments-str"></a>

One of: disabled, members, observers, org or public

##### prefs_invitations: `str`<a id="prefs_invitations-str"></a>

One of: admins or members

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: org, private or public

##### prefs_self_join: `str`<a id="prefs_self_join-str"></a>

 true or false

##### prefs_voting: `str`<a id="prefs_voting-str"></a>

One of: disabled, members, observers, org or public

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Boards`](./trello_python_sdk/type/boards.py)
Attributes of \"Boards\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.create_lists_by_id_board`<a id="trelloboardcreate_lists_by_id_board"></a>

addBoardsListsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.create_lists_by_id_board(
    id_board="idBoard_example",
    name="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsLists`](./trello_python_sdk/type/boards_lists.py)
Attributes of \"Boards Lists\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/lists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.filter_cards_by_id_board`<a id="trelloboardfilter_cards_by_id_board"></a>

getBoardsCardsByIdBoardByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.filter_cards_by_id_board(
    id_board="idBoard_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/cards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.generate_calendar_key_by_id`<a id="trelloboardgenerate_calendar_key_by_id"></a>

addBoardsCalendarKeyGenerateByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.generate_calendar_key_by_id(
    id_board="idBoard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/calendarKey/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.generate_email_key`<a id="trelloboardgenerate_email_key"></a>

addBoardsEmailKeyGenerateByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.generate_email_key(
    id_board="idBoard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/emailKey/generate` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_board_stars_by_id`<a id="trelloboardget_board_stars_by_id"></a>

getBoardsBoardStarsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_board_stars_by_id(
    id_board="idBoard_example",
    filter="mine",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

One of: mine or none

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/boardStars` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_by_id`<a id="trelloboardget_by_id"></a>

getBoardsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_by_id(
    id_board="idBoard_example",
    actions="string_example",
    actions_entities="string_example",
    actions_display="string_example",
    actions_format="list",
    actions_since="string_example",
    actions_limit="50",
    action_fields="all",
    action_member="string_example",
    action_member_fields="avatarHash, fullName, initials and username",
    action_member_creator="string_example",
    action_member_creator_fields="avatarHash, fullName, initials and username",
    cards="none",
    card_fields="all",
    card_attachments="string_example",
    card_attachment_fields="all",
    card_checklists="none",
    card_stickers="string_example",
    board_stars="none",
    labels="none",
    label_fields="all",
    labels_limit="50",
    lists="none",
    list_fields="all",
    memberships="none",
    memberships_member="string_example",
    memberships_member_fields="fullName and username",
    members="none",
    member_fields="avatarHash, initials, fullName, username and confirmed",
    members_invited="none",
    members_invited_fields="avatarHash, initials, fullName and username",
    checklists="none",
    checklist_fields="all",
    organization="string_example",
    organization_fields="name and displayName",
    organization_memberships="none",
    my_prefs="string_example",
    fields="name, desc, descData, closed, idOrganization, pinned, url, shortUrl, prefs and labelNames",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_display: `str`<a id="actions_display-str"></a>

 true or false

##### actions_format: `str`<a id="actions_format-str"></a>

One of: count, list or minimal

##### actions_since: `str`<a id="actions_since-str"></a>

A date, null or lastView

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### action_member: `str`<a id="action_member-str"></a>

 true or false

##### action_member_fields: `str`<a id="action_member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### action_member_creator: `str`<a id="action_member_creator-str"></a>

 true or false

##### action_member_creator_fields: `str`<a id="action_member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### card_attachments: `str`<a id="card_attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### card_attachment_fields: `str`<a id="card_attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### card_checklists: `str`<a id="card_checklists-str"></a>

One of: all or none

##### card_stickers: `str`<a id="card_stickers-str"></a>

 true or false

##### board_stars: `str`<a id="board_stars-str"></a>

One of: mine or none

##### labels: `str`<a id="labels-str"></a>

One of: all or none

##### label_fields: `str`<a id="label_fields-str"></a>

all or a comma-separated list of: color, idBoard, name or uses

##### labels_limit: `str`<a id="labels_limit-str"></a>

a number from 0 to 1000

##### lists: `str`<a id="lists-str"></a>

One of: all, closed, none or open

##### list_fields: `str`<a id="list_fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

##### memberships: `str`<a id="memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### memberships_member: `str`<a id="memberships_member-str"></a>

 true or false

##### memberships_member_fields: `str`<a id="memberships_member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members: `str`<a id="members-str"></a>

One of: admins, all, none, normal or owners

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members_invited: `str`<a id="members_invited-str"></a>

One of: admins, all, none, normal or owners

##### members_invited_fields: `str`<a id="members_invited_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### checklist_fields: `str`<a id="checklist_fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

##### organization: `str`<a id="organization-str"></a>

 true or false

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### organization_memberships: `str`<a id="organization_memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### my_prefs: `str`<a id="my_prefs-str"></a>

 true or false

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_by_id_field`<a id="trelloboardget_by_id_field"></a>

getBoardsByIdBoardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_by_id_field(
    id_board="idBoard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_cards_by_id_board`<a id="trelloboardget_cards_by_id_board"></a>

getBoardsCardsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_cards_by_id_board(
    id_board="idBoard_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    stickers="string_example",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    limit="string_example",
    since="string_example",
    before="string_example",
    filter="visible",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### stickers: `str`<a id="stickers-str"></a>

 true or false

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 1000

##### since: `str`<a id="since-str"></a>

A date, or null

##### before: `str`<a id="before-str"></a>

A date, or null

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none, open or visible

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_cards_by_id_board_by_id_card`<a id="trelloboardget_cards_by_id_board_by_id_card"></a>

getBoardsCardsByIdBoardByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_cards_by_id_board_by_id_card(
    id_board="idBoard_example",
    id_card="idCard_example",
    attachments="string_example",
    attachment_fields="all",
    actions="string_example",
    actions_entities="string_example",
    actions_display="string_example",
    actions_limit="50",
    action_fields="all",
    action_member_creator_fields="avatarHash, fullName, initials and username",
    members="string_example",
    member_fields="avatarHash, initials, fullName and username",
    check_item_states="string_example",
    check_item_state_fields="all",
    labels="string_example",
    checklists="none",
    checklist_fields="all",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_card: `str`<a id="id_card-str"></a>

idCard

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_display: `str`<a id="actions_display-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### action_member_creator_fields: `str`<a id="action_member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### check_item_state_fields: `str`<a id="check_item_state_fields-str"></a>

all or a comma-separated list of: idCheckItem or state

##### labels: `str`<a id="labels-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### checklist_fields: `str`<a id="checklist_fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/cards/{idCard}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_checklists_by_id`<a id="trelloboardget_checklists_by_id"></a>

getBoardsChecklistsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_checklists_by_id(
    id_board="idBoard_example",
    cards="none",
    card_fields="all",
    check_items="all",
    check_item_fields="name, nameData, pos and state",
    filter="all",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### check_items: `str`<a id="check_items-str"></a>

One of: all or none

##### check_item_fields: `str`<a id="check_item_fields-str"></a>

all or a comma-separated list of: name, nameData, pos, state or type

##### filter: `str`<a id="filter-str"></a>

One of: all or none

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/checklists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_deltas_by_id_board`<a id="trelloboardget_deltas_by_id_board"></a>

getBoardsDeltasByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_deltas_by_id_board(
    id_board="idBoard_example",
    tags="tags_example",
    ix_last_update="ixLastUpdate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### tags: `str`<a id="tags-str"></a>

A valid tag for subscribing

##### ix_last_update: `str`<a id="ix_last_update-str"></a>

a number from -1 to Infinity

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/deltas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_labels_by_id_board_by_id_label`<a id="trelloboardget_labels_by_id_board_by_id_label"></a>

getBoardsLabelsByIdBoardByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_labels_by_id_board_by_id_label(
    id_board="idBoard_example",
    id_label="idLabel_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: color, idBoard, name or uses

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labels/{idLabel}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_lists_by_filter`<a id="trelloboardget_lists_by_filter"></a>

getBoardsListsByIdBoardByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_lists_by_filter(
    id_board="idBoard_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/lists/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_lists_by_id_board`<a id="trelloboardget_lists_by_id_board"></a>

getBoardsListsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_lists_by_id_board(
    id_board="idBoard_example",
    cards="none",
    card_fields="all",
    filter="open",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none or open

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/lists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_members_by_filter`<a id="trelloboardget_members_by_filter"></a>

getBoardsMembersByIdBoardByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_members_by_filter(
    id_board="idBoard_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_members_by_id_board`<a id="trelloboardget_members_by_id_board"></a>

getBoardsMembersByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_members_by_id_board(
    id_board="idBoard_example",
    filter="all",
    fields="fullName and username",
    activity="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

One of: admins, all, none, normal or owners

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### activity: `str`<a id="activity-str"></a>

true or false ; works for premium organizations only.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_members_cards_by_id_board_by_id_member`<a id="trelloboardget_members_cards_by_id_board_by_id_member"></a>

getBoardsMembersCardsByIdBoardByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_members_cards_by_id_board_by_id_member(
    id_board="idBoard_example",
    id_member="idMember_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    board="string_example",
    board_fields="name, desc, closed, idOrganization, pinned, url and prefs",
    _list="string_example",
    list_fields="all",
    filter="visible",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_member: `str`<a id="id_member-str"></a>

idMember

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### board: `str`<a id="board-str"></a>

 true or false

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### _list: `str`<a id="_list-str"></a>

 true or false

##### list_fields: `str`<a id="list_fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none, open or visible

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members/{idMember}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_members_invited_by_field`<a id="trelloboardget_members_invited_by_field"></a>

getBoardsMembersInvitedByIdBoardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_members_invited_by_field(
    id_board="idBoard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/membersInvited/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_members_invited_by_id_board`<a id="trelloboardget_members_invited_by_id_board"></a>

getBoardsMembersInvitedByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_members_invited_by_id_board(
    id_board="idBoard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/membersInvited` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_memberships_by_id_board`<a id="trelloboardget_memberships_by_id_board"></a>

getBoardsMembershipsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_memberships_by_id_board(
    id_board="idBoard_example",
    filter="all",
    member="string_example",
    member_fields="fullName and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_memberships_by_id_board_by_id_membership`<a id="trelloboardget_memberships_by_id_board_by_id_membership"></a>

getBoardsMembershipsByIdBoardByIdMembership()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_memberships_by_id_board_by_id_membership(
    id_board="idBoard_example",
    id_membership="idMembership_example",
    member="string_example",
    member_fields="fullName and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_membership: `str`<a id="id_membership-str"></a>

idMembership

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/memberships/{idMembership}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_my_prefs_by_id`<a id="trelloboardget_my_prefs_by_id"></a>

getBoardsMyPrefsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_my_prefs_by_id(
    id_board="idBoard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_organization_by_id`<a id="trelloboardget_organization_by_id"></a>

getBoardsOrganizationByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_organization_by_id(
    id_board="idBoard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/organization` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.get_organization_by_id_board_by_field`<a id="trelloboardget_organization_by_id_board_by_field"></a>

getBoardsOrganizationByIdBoardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.get_organization_by_id_board_by_field(
    id_board="idBoard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/organization/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.list_actions_by_id_board`<a id="trelloboardlist_actions_by_id_board"></a>

getBoardsActionsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.list_actions_by_id_board(
    id_board="idBoard_example",
    entities="string_example",
    display="string_example",
    filter="all",
    fields="all",
    limit="50",
    format="list",
    since="string_example",
    before="string_example",
    page="0",
    id_models="string_example",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

##### format: `str`<a id="format-str"></a>

One of: count, list or minimal

##### since: `str`<a id="since-str"></a>

A date, null or lastView

##### before: `str`<a id="before-str"></a>

A date, or null

##### page: `str`<a id="page-str"></a>

Page * limit must be less than 1000

##### id_models: `str`<a id="id_models-str"></a>

Only return actions related to these model ids

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.list_labels_by_id_board`<a id="trelloboardlist_labels_by_id_board"></a>

getBoardsLabelsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.list_labels_by_id_board(
    id_board="idBoard_example",
    fields="all",
    limit="50",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: color, idBoard, name or uses

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labels` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.mark_as_viewed_by_id_board`<a id="trelloboardmark_as_viewed_by_id_board"></a>

addBoardsMarkAsViewedByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.mark_as_viewed_by_id_board(
    id_board="idBoard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/markAsViewed` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.remove_member`<a id="trelloboardremove_member"></a>

deleteBoardsMembersByIdBoardByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.remove_member(
    id_board="idBoard_example",
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_member: `str`<a id="id_member-str"></a>

idMember

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members/{idMember}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.remove_power_up`<a id="trelloboardremove_power_up"></a>

deleteBoardsPowerUpsByIdBoardByPowerUp()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.remove_power_up(
    id_board="idBoard_example",
    power_up="powerUp_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### power_up: `str`<a id="power_up-str"></a>

powerUp

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/powerUps/{powerUp}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_by_id`<a id="trelloboardupdate_by_id"></a>

updateBoardsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_by_id(
    id_board="idBoard_example",
    closed="string_example",
    desc="string_example",
    id_board_source="string_example",
    id_organization="string_example",
    keep_from_source="string_example",
    label_names_blue="string_example",
    label_names_green="string_example",
    label_names_orange="string_example",
    label_names_purple="string_example",
    label_names_red="string_example",
    label_names_yellow="string_example",
    name="string_example",
    power_ups="string_example",
    prefs_background="string_example",
    prefs_calendar_feed_enabled="string_example",
    prefs_card_aging="string_example",
    prefs_card_covers="string_example",
    prefs_comments="string_example",
    prefs_invitations="string_example",
    prefs_permission_level="string_example",
    prefs_self_join="string_example",
    prefs_voting="string_example",
    prefs_background="string_example",
    prefs_card_aging="string_example",
    prefs_card_covers="string_example",
    prefs_comments="string_example",
    prefs_invitations="string_example",
    prefs_permission_level="string_example",
    prefs_self_join="string_example",
    prefs_voting="string_example",
    subscribed="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### closed: `str`<a id="closed-str"></a>

 true or false

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### id_board_source: `str`<a id="id_board_source-str"></a>

The id of the board to copy into the new board

##### id_organization: `str`<a id="id_organization-str"></a>

The id or name of the organization to add the board to.

##### keep_from_source: `str`<a id="keep_from_source-str"></a>

Components of the source board to copy.

##### label_names_blue: `str`<a id="label_names_blue-str"></a>

a string with a length from 0 to 16384

##### label_names_green: `str`<a id="label_names_green-str"></a>

a string with a length from 0 to 16384

##### label_names_orange: `str`<a id="label_names_orange-str"></a>

a string with a length from 0 to 16384

##### label_names_purple: `str`<a id="label_names_purple-str"></a>

a string with a length from 0 to 16384

##### label_names_red: `str`<a id="label_names_red-str"></a>

a string with a length from 0 to 16384

##### label_names_yellow: `str`<a id="label_names_yellow-str"></a>

a string with a length from 0 to 16384

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### power_ups: `str`<a id="power_ups-str"></a>

all or a comma-separated list of: calendar, cardAging, recap or voting

##### prefs_background: `str`<a id="prefs_background-str"></a>

A standard background name, or the id of a custom background

##### prefs_calendar_feed_enabled: `str`<a id="prefs_calendar_feed_enabled-str"></a>

 true or false

##### prefs_card_aging: `str`<a id="prefs_card_aging-str"></a>

One of: pirate or regular

##### prefs_card_covers: `str`<a id="prefs_card_covers-str"></a>

 true or false

##### prefs_comments: `str`<a id="prefs_comments-str"></a>

One of: disabled, members, observers, org or public

##### prefs_invitations: `str`<a id="prefs_invitations-str"></a>

One of: admins or members

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: org, private or public

##### prefs_self_join: `str`<a id="prefs_self_join-str"></a>

 true or false

##### prefs_voting: `str`<a id="prefs_voting-str"></a>

One of: disabled, members, observers, org or public

##### prefs_background: `str`<a id="prefs_background-str"></a>

a string with a length from 0 to 16384

##### prefs_card_aging: `str`<a id="prefs_card_aging-str"></a>

One of: pirate or regular

##### prefs_card_covers: `str`<a id="prefs_card_covers-str"></a>

 true or false

##### prefs_comments: `str`<a id="prefs_comments-str"></a>

One of: disabled, members, observers, org or public

##### prefs_invitations: `str`<a id="prefs_invitations-str"></a>

One of: admins or members

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: org, private or public

##### prefs_self_join: `str`<a id="prefs_self_join-str"></a>

 true or false

##### prefs_voting: `str`<a id="prefs_voting-str"></a>

One of: disabled, members, observers, org or public

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Boards`](./trello_python_sdk/type/boards.py)
Attributes of \"Boards\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_closed_by_id`<a id="trelloboardupdate_closed_by_id"></a>

updateBoardsClosedByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_closed_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsClosed`](./trello_python_sdk/type/boards_closed.py)
Attributes of \"Boards Closed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/closed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_description_by_id_board`<a id="trelloboardupdate_description_by_id_board"></a>

updateBoardsDescByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_description_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsDesc`](./trello_python_sdk/type/boards_desc.py)
Attributes of \"Boards Desc\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/desc` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_blue_by_id`<a id="trelloboardupdate_label_names_blue_by_id"></a>

updateBoardsLabelNamesBlueByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_blue_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesBlue`](./trello_python_sdk/type/label_names_blue.py)
Attributes of \"Label Names Blue\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/blue` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_green_by_id_board_put`<a id="trelloboardupdate_label_names_green_by_id_board_put"></a>

updateBoardsLabelNamesGreenByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_green_by_id_board_put(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesGreen`](./trello_python_sdk/type/label_names_green.py)
Attributes of \"Label Names Green\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/green` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_orange_by_id_board`<a id="trelloboardupdate_label_names_orange_by_id_board"></a>

updateBoardsLabelNamesOrangeByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_orange_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesOrange`](./trello_python_sdk/type/label_names_orange.py)
Attributes of \"Label Names Orange\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/orange` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_purple_by_id_board`<a id="trelloboardupdate_label_names_purple_by_id_board"></a>

updateBoardsLabelNamesPurpleByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_purple_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesPurple`](./trello_python_sdk/type/label_names_purple.py)
Attributes of \"Label Names Purple\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/purple` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_red`<a id="trelloboardupdate_label_names_red"></a>

updateBoardsLabelNamesRedByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_red(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesRed`](./trello_python_sdk/type/label_names_red.py)
Attributes of \"Label Names Red\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/red` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_label_names_yellow_by_id_board`<a id="trelloboardupdate_label_names_yellow_by_id_board"></a>

updateBoardsLabelNamesYellowByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_label_names_yellow_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelNamesYellow`](./trello_python_sdk/type/label_names_yellow.py)
Attributes of \"Label Names Yellow\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/labelNames/yellow` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_members_by_id_board`<a id="trelloboardupdate_members_by_id_board"></a>

updateBoardsMembersByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_members_by_id_board(
    id_board="idBoard_example",
    email="string_example",
    full_name="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### email: `str`<a id="email-str"></a>

An email address

##### full_name: `str`<a id="full_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsMembers`](./trello_python_sdk/type/boards_members.py)
Attributes of \"Boards Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_members_by_id_board_by_id_member`<a id="trelloboardupdate_members_by_id_board_by_id_member"></a>

updateBoardsMembersByIdBoardByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_members_by_id_board_by_id_member(
    id_board="idBoard_example",
    id_member="idMember_example",
    email="string_example",
    full_name="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_member: `str`<a id="id_member-str"></a>

idMember

##### email: `str`<a id="email-str"></a>

An email address

##### full_name: `str`<a id="full_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsMembers`](./trello_python_sdk/type/boards_members.py)
Attributes of \"Boards Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/members/{idMember}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_memberships_by_id_board_by_id_membership`<a id="trelloboardupdate_memberships_by_id_board_by_id_membership"></a>

updateBoardsMembershipsByIdBoardByIdMembership()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_memberships_by_id_board_by_id_membership(
    id_board="idBoard_example",
    id_membership="idMembership_example",
    member_fields="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### id_membership: `str`<a id="id_membership-str"></a>

idMembership

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsMemberships`](./trello_python_sdk/type/boards_memberships.py)
Attributes of \"Boards Memberships\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/memberships/{idMembership}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_email_list_by_id_board`<a id="trelloboardupdate_my_prefs_email_list_by_id_board"></a>

updateBoardsMyPrefsIdEmailListByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_email_list_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

An id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsIdEmailList`](./trello_python_sdk/type/my_prefs_id_email_list.py)
Attributes of \"My Prefs Id Email List\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/idEmailList` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_email_position_by_id_board`<a id="trelloboardupdate_my_prefs_email_position_by_id_board"></a>

updateBoardsMyPrefsEmailPositionByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_email_position_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: bottom or top

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsEmailPosition`](./trello_python_sdk/type/my_prefs_email_position.py)
Attributes of \"My Prefs Email Position\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/emailPosition` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_show_list_guide_by_id_board`<a id="trelloboardupdate_my_prefs_show_list_guide_by_id_board"></a>

updateBoardsMyPrefsShowListGuideByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_show_list_guide_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsShowListGuide`](./trello_python_sdk/type/my_prefs_show_list_guide.py)
Attributes of \"My Prefs Show List Guide\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/showListGuide` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_show_sidebar`<a id="trelloboardupdate_my_prefs_show_sidebar"></a>

updateBoardsMyPrefsShowSidebarByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_show_sidebar(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsShowSidebar`](./trello_python_sdk/type/my_prefs_show_sidebar.py)
Attributes of \"My Prefs Show Sidebar\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/showSidebar` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_show_sidebar_actions_by_id_board`<a id="trelloboardupdate_my_prefs_show_sidebar_actions_by_id_board"></a>

updateBoardsMyPrefsShowSidebarBoardActionsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_show_sidebar_actions_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsShowSidebarBoardActions`](./trello_python_sdk/type/my_prefs_show_sidebar_board_actions.py)
Attributes of \"My Prefs Show Sidebar Board Actions\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/showSidebarBoardActions` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_my_prefs_show_sidebar_activity_by_id_board`<a id="trelloboardupdate_my_prefs_show_sidebar_activity_by_id_board"></a>

updateBoardsMyPrefsShowSidebarActivityByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_my_prefs_show_sidebar_activity_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsShowSidebarActivity`](./trello_python_sdk/type/my_prefs_show_sidebar_activity.py)
Attributes of \"My Prefs Show Sidebar Activity\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/showSidebarActivity` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_name_by_id`<a id="trelloboardupdate_name_by_id"></a>

updateBoardsNameByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_name_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsName`](./trello_python_sdk/type/boards_name.py)
Attributes of \"Boards Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_organization_by_id_board`<a id="trelloboardupdate_organization_by_id_board"></a>

updateBoardsIdOrganizationByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_organization_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsIdOrganization`](./trello_python_sdk/type/boards_id_organization.py)
Attributes of \"Boards Id Organization\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/idOrganization` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_background_by_id_board`<a id="trelloboardupdate_prefs_background_by_id_board"></a>

updateBoardsPrefsBackgroundByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_background_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

A standard background name, or the id of a custom background

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsBackground`](./trello_python_sdk/type/prefs_background.py)
Attributes of \"Prefs Background\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/background` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_calendar_feed_enabled_by_id`<a id="trelloboardupdate_prefs_calendar_feed_enabled_by_id"></a>

updateBoardsPrefsCalendarFeedEnabledByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_calendar_feed_enabled_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsCalendarFeedEnabled`](./trello_python_sdk/type/prefs_calendar_feed_enabled.py)
Attributes of \"Prefs Calendar Feed Enabled\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/calendarFeedEnabled` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_card_aging_by_id_board`<a id="trelloboardupdate_prefs_card_aging_by_id_board"></a>

updateBoardsPrefsCardAgingByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_card_aging_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: pirate or regular

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsCardAging`](./trello_python_sdk/type/prefs_card_aging.py)
Attributes of \"Prefs Card Aging\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/cardAging` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_card_covers_by_id_board`<a id="trelloboardupdate_prefs_card_covers_by_id_board"></a>

updateBoardsPrefsCardCoversByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_card_covers_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsCardCovers`](./trello_python_sdk/type/prefs_card_covers.py)
Attributes of \"Prefs Card Covers\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/cardCovers` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_comments_by_id_board`<a id="trelloboardupdate_prefs_comments_by_id_board"></a>

updateBoardsPrefsCommentsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_comments_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: disabled, members, observers, org or public

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsComments`](./trello_python_sdk/type/prefs_comments.py)
Attributes of \"Prefs Comments\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/comments` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_invitations_by_id_board`<a id="trelloboardupdate_prefs_invitations_by_id_board"></a>

updateBoardsPrefsInvitationsByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_invitations_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: admins or members

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsInvitations`](./trello_python_sdk/type/prefs_invitations.py)
Attributes of \"Prefs Invitations\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/invitations` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_permission_level_by_id`<a id="trelloboardupdate_prefs_permission_level_by_id"></a>

updateBoardsPrefsPermissionLevelByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_permission_level_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: private or public

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsPermissionLevel`](./trello_python_sdk/type/prefs_permission_level.py)
Attributes of \"Prefs Permission Level\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/permissionLevel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_self_join_by_id_board`<a id="trelloboardupdate_prefs_self_join_by_id_board"></a>

updateBoardsPrefsSelfJoinByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_self_join_by_id_board(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsSelfJoin`](./trello_python_sdk/type/prefs_self_join.py)
Attributes of \"Prefs Self Join\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/selfJoin` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_prefs_show_sidebar_members_by_id`<a id="trelloboardupdate_prefs_show_sidebar_members_by_id"></a>

updateBoardsMyPrefsShowSidebarMembersByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_prefs_show_sidebar_members_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MyPrefsShowSidebarMembers`](./trello_python_sdk/type/my_prefs_show_sidebar_members.py)
Attributes of \"My Prefs Show Sidebar Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/myPrefs/showSidebarMembers` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_subscribed_by_id`<a id="trelloboardupdate_subscribed_by_id"></a>

updateBoardsSubscribedByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_subscribed_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`BoardsSubscribed`](./trello_python_sdk/type/boards_subscribed.py)
Attributes of \"Boards Subscribed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/subscribed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.board.update_voting_prefs_by_id`<a id="trelloboardupdate_voting_prefs_by_id"></a>

updateBoardsPrefsVotingByIdBoard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.board.update_voting_prefs_by_id(
    id_board="idBoard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

board_id

##### value: `str`<a id="value-str"></a>

One of: disabled, members, observers, org or public

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsVoting`](./trello_python_sdk/type/prefs_voting.py)
Attributes of \"Prefs Voting\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/boards/{idBoard}/prefs/voting` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_actions_comments_by_id_card`<a id="trellocardadd_actions_comments_by_id_card"></a>

addCardsActionsCommentsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_actions_comments_by_id_card(
    id_card="idCard_example",
    text="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### text: `str`<a id="text-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ActionsComments`](./trello_python_sdk/type/actions_comments.py)
Attributes of \"Actions Comments\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/actions/comments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_attachments_by_id_card`<a id="trellocardadd_attachments_by_id_card"></a>

addCardsAttachmentsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_attachments_by_id_card(
    id_card="idCard_example",
    file="string_example",
    mime_type="string_example",
    name="string_example",
    url="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### file: `str`<a id="file-str"></a>

A file

##### mime_type: `str`<a id="mime_type-str"></a>

a string with a length from 0 to 256

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 256

##### url: `str`<a id="url-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsAttachments`](./trello_python_sdk/type/cards_attachments.py)
Attributes of \"Cards Attachments\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/attachments` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_checklist_check_item`<a id="trellocardadd_checklist_check_item"></a>

addCardsChecklistCheckItemByIdCardByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_checklist_check_item(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    name="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklistCheckItem`](./trello_python_sdk/type/cards_checklist_check_item.py)
Attributes of \"Cards Checklist Check Item\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_checklists`<a id="trellocardadd_checklists"></a>

addCardsChecklistsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_checklists(
    id_card="idCard_example",
    id_checklist_source="string_example",
    name="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist_source: `str`<a id="id_checklist_source-str"></a>

The id of the source checklist to copy into a new checklist.

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### value: `str`<a id="value-str"></a>

The id of the checklist to add to the card, or null to create a new one.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklists`](./trello_python_sdk/type/cards_checklists.py)
Attributes of \"Cards Checklists\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_id_labels_to_card`<a id="trellocardadd_id_labels_to_card"></a>

addCardsIdLabelsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_id_labels_to_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

The id of the label to add

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdLabels`](./trello_python_sdk/type/cards_id_labels.py)
Attributes of \"Cards Id Labels\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idLabels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_labels`<a id="trellocardadd_labels"></a>

addCardsLabelsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_labels(
    id_card="idCard_example",
    color="string_example",
    name="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### color: `str`<a id="color-str"></a>

A valid label color or null

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### value: `str`<a id="value-str"></a>

all or a comma-separated list of: blue, green, orange, purple, red or yellow

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsLabels`](./trello_python_sdk/type/cards_labels.py)
Attributes of \"Cards Labels\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/labels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_members`<a id="trellocardadd_members"></a>

addCardsIdMembersByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_members(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

The id of the member to add to the card

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdMembers`](./trello_python_sdk/type/cards_id_members.py)
Attributes of \"Cards Id Members\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idMembers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_members_voted`<a id="trellocardadd_members_voted"></a>

addCardsMembersVotedByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_members_voted(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

The id of the member to vote &#39;yes&#39; on the card

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsMembersVoted`](./trello_python_sdk/type/cards_members_voted.py)
Attributes of \"Cards Members Voted\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/membersVoted` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.add_stickers_by_id_card`<a id="trellocardadd_stickers_by_id_card"></a>

addCardsStickersByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.add_stickers_by_id_card(
    id_card="idCard_example",
    image="string_example",
    left="string_example",
    rotate="string_example",
    top="string_example",
    z_index="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### image: `str`<a id="image-str"></a>

a string with a length from 0 to 16384

##### left: `str`<a id="left-str"></a>

undefined

##### rotate: `str`<a id="rotate-str"></a>

undefined

##### top: `str`<a id="top-str"></a>

undefined

##### z_index: `str`<a id="z_index-str"></a>

Valid Z values for stickers, must be an integer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsStickers`](./trello_python_sdk/type/cards_stickers.py)
Attributes of \"Cards Stickers\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/stickers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.convert_check_item_to_card`<a id="trellocardconvert_check_item_to_card"></a>

addCardsChecklistCheckItemConvertToCardByIdCardByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.convert_check_item_to_card(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/convertToCard` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.create_and_update`<a id="trellocardcreate_and_update"></a>

addCards()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.create_and_update(
    closed="string_example",
    desc="string_example",
    due="string_example",
    file_source="string_example",
    id_attachment_cover="string_example",
    id_board="string_example",
    id_card_source="string_example",
    id_labels="string_example",
    id_list="string_example",
    id_members="string_example",
    keep_from_source="string_example",
    labels="string_example",
    name="string_example",
    pos="string_example",
    subscribed="string_example",
    url_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### closed: `str`<a id="closed-str"></a>

 true or false

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### due: `str`<a id="due-str"></a>

A date, or null

##### file_source: `str`<a id="file_source-str"></a>

A file

##### id_attachment_cover: `str`<a id="id_attachment_cover-str"></a>

Id of the image attachment of this card to use as its cover, or null for no cover

##### id_board: `str`<a id="id_board-str"></a>

id of the board the card should be moved to

##### id_card_source: `str`<a id="id_card_source-str"></a>

The id of the card to copy into a new card.

##### id_labels: `str`<a id="id_labels-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### id_list: `str`<a id="id_list-str"></a>

id of the list that the card should be added to

##### id_members: `str`<a id="id_members-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### keep_from_source: `str`<a id="keep_from_source-str"></a>

Properties of the card to copy over from the source.

##### labels: `str`<a id="labels-str"></a>

all or a comma-separated list of: blue, green, orange, purple, red or yellow

##### name: `str`<a id="name-str"></a>

The name of the new card.  It isn&#39;t required if the name is being copied from provided by a URL, file or card that is being copied.

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

##### url_source: `str`<a id="url_source-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Cards`](./trello_python_sdk/type/cards.py)
Attributes of \"Cards\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.delete_attachments_by_id_card_by_id_attachment`<a id="trellocarddelete_attachments_by_id_card_by_id_attachment"></a>

deleteCardsAttachmentsByIdCardByIdAttachment()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.delete_attachments_by_id_card_by_id_attachment(
    id_card="idCard_example",
    id_attachment="idAttachment_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_attachment: `str`<a id="id_attachment-str"></a>

idAttachment

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/attachments/{idAttachment}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.delete_checklist_by_id_card_by_id_checklist`<a id="trellocarddelete_checklist_by_id_card_by_id_checklist"></a>

deleteCardsChecklistsByIdCardByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.delete_checklist_by_id_card_by_id_checklist(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklists/{idChecklist}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_attachments_by_id_card`<a id="trellocardget_attachments_by_id_card"></a>

getCardsAttachmentsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_attachments_by_id_card(
    id_card="idCard_example",
    fields="all",
    filter="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### filter: `str`<a id="filter-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/attachments` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_attachments_by_ids`<a id="trellocardget_attachments_by_ids"></a>

getCardsAttachmentsByIdCardByIdAttachment()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_attachments_by_ids(
    id_card="idCard_example",
    id_attachment="idAttachment_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_attachment: `str`<a id="id_attachment-str"></a>

idAttachment

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/attachments/{idAttachment}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_board_by_id`<a id="trellocardget_board_by_id"></a>

getCardsBoardByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_board_by_id(
    id_card="idCard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_board_by_id_card_by_field`<a id="trellocardget_board_by_id_card_by_field"></a>

getCardsBoardByIdCardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_board_by_id_card_by_field(
    id_card="idCard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_by_id`<a id="trellocardget_by_id"></a>

getCardsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_by_id(
    id_card="idCard_example",
    actions="string_example",
    actions_entities="string_example",
    actions_display="string_example",
    actions_limit="50",
    action_fields="all",
    action_member_creator_fields="avatarHash, fullName, initials and username",
    attachments="string_example",
    attachment_fields="all",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    members_voted="string_example",
    member_voted_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    check_item_state_fields="all",
    checklists="none",
    checklist_fields="all",
    board="string_example",
    board_fields="name, desc, descData, closed, idOrganization, pinned, url and prefs",
    _list="string_example",
    list_fields="all",
    stickers="string_example",
    sticker_fields="all",
    fields="badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idBoard, idChecklists, idLabels, idList, idMembers, idShort, idAttachmentCover, manualCoverAttachment, labels, name, pos, shortUrl and url",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_display: `str`<a id="actions_display-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### action_member_creator_fields: `str`<a id="action_member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members_voted: `str`<a id="members_voted-str"></a>

 true or false

##### member_voted_fields: `str`<a id="member_voted_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### check_item_state_fields: `str`<a id="check_item_state_fields-str"></a>

all or a comma-separated list of: idCheckItem or state

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### checklist_fields: `str`<a id="checklist_fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

##### board: `str`<a id="board-str"></a>

 true or false

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### _list: `str`<a id="_list-str"></a>

 true or false

##### list_fields: `str`<a id="list_fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

##### stickers: `str`<a id="stickers-str"></a>

 true or false

##### sticker_fields: `str`<a id="sticker_fields-str"></a>

all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_by_id_field`<a id="trellocardget_by_id_field"></a>

getCardsByIdCardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_by_id_field(
    id_card="idCard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_cards_list_by_id_card_by_field`<a id="trellocardget_cards_list_by_id_card_by_field"></a>

getCardsListByIdCardByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_cards_list_by_id_card_by_field(
    id_card="idCard_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/list/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_check_item_states_by_id`<a id="trellocardget_check_item_states_by_id"></a>

getCardsCheckItemStatesByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_check_item_states_by_id(
    id_card="idCard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: idCheckItem or state

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checkItemStates` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_checklists_by_id`<a id="trellocardget_checklists_by_id"></a>

getCardsChecklistsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_checklists_by_id(
    id_card="idCard_example",
    cards="none",
    card_fields="all",
    check_items="all",
    check_item_fields="name, nameData, pos and state",
    filter="all",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### check_items: `str`<a id="check_items-str"></a>

One of: all or none

##### check_item_fields: `str`<a id="check_item_fields-str"></a>

all or a comma-separated list of: name, nameData, pos, state or type

##### filter: `str`<a id="filter-str"></a>

One of: all or none

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklists` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_list_by_id`<a id="trellocardget_list_by_id"></a>

getCardsListByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_list_by_id(
    id_card="idCard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_members_voted_by_id_card`<a id="trellocardget_members_voted_by_id_card"></a>

getCardsMembersVotedByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_members_voted_by_id_card(
    id_card="idCard_example",
    fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/membersVoted` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_sticker_by_ids`<a id="trellocardget_sticker_by_ids"></a>

getCardsStickersByIdCardByIdSticker()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_sticker_by_ids(
    id_card="idCard_example",
    id_sticker="idSticker_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_sticker: `str`<a id="id_sticker-str"></a>

idSticker

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/stickers/{idSticker}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.get_stickers_by_id_card`<a id="trellocardget_stickers_by_id_card"></a>

getCardsStickersByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.get_stickers_by_id_card(
    id_card="idCard_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: image, imageScaled, imageUrl, left, rotate, top or zIndex

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/stickers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.list_card_actions_by_id`<a id="trellocardlist_card_actions_by_id"></a>

getCardsActionsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.list_card_actions_by_id(
    id_card="idCard_example",
    entities="string_example",
    display="string_example",
    filter="commentCard and updateCard:idList",
    fields="all",
    limit="50",
    format="list",
    since="string_example",
    before="string_example",
    page="0",
    id_models="string_example",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

##### format: `str`<a id="format-str"></a>

One of: count, list or minimal

##### since: `str`<a id="since-str"></a>

A date, null or lastView

##### before: `str`<a id="before-str"></a>

A date, or null

##### page: `str`<a id="page-str"></a>

Page * limit must be less than 1000

##### id_models: `str`<a id="id_models-str"></a>

Only return actions related to these model ids

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.list_members_by_id_card`<a id="trellocardlist_members_by_id_card"></a>

getCardsMembersByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.list_members_by_id_card(
    id_card="idCard_example",
    fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.mark_associated_notifications_read`<a id="trellocardmark_associated_notifications_read"></a>

addCardsMarkAssociatedNotificationsReadByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.mark_associated_notifications_read(
    id_card="idCard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/markAssociatedNotificationsRead` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_action_comment_by_id_card_by_id_action`<a id="trellocardremove_action_comment_by_id_card_by_id_action"></a>

This can only be done by the original author of the comment, or someone with higher permissions than the original author.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_action_comment_by_id_card_by_id_action(
    id_card="idCard_example",
    id_action="idAction_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_action: `str`<a id="id_action-str"></a>

idAction

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/actions/{idAction}/comments` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_by_id_card`<a id="trellocardremove_by_id_card"></a>

deleteCardsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_by_id_card(
    id_card="idCard_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_checklist_check_item`<a id="trellocardremove_checklist_check_item"></a>

deleteCardsChecklistCheckItemByIdCardByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_checklist_check_item(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_label_by_id_card_by_id_label`<a id="trellocardremove_label_by_id_card_by_id_label"></a>

deleteCardsIdLabelsByIdCardByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_label_by_id_card_by_id_label(
    id_card="idCard_example",
    id_label="idLabel_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_label: `str`<a id="id_label-str"></a>

idLabel

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idLabels/{idLabel}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_labels_by_id_card_by_color`<a id="trellocardremove_labels_by_id_card_by_color"></a>

deleteCardsLabelsByIdCardByColor()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_labels_by_id_card_by_color(
    id_card="idCard_example",
    color="color_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### color: `str`<a id="color-str"></a>

color

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/labels/{color}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_member_by_id_member`<a id="trellocardremove_member_by_id_member"></a>

deleteCardsIdMembersByIdCardByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_member_by_id_member(
    id_card="idCard_example",
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_member: `str`<a id="id_member-str"></a>

idMember

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idMembers/{idMember}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_members_voted_by_id_card_by_id_member`<a id="trellocardremove_members_voted_by_id_card_by_id_member"></a>

deleteCardsMembersVotedByIdCardByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_members_voted_by_id_card_by_id_member(
    id_card="idCard_example",
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_member: `str`<a id="id_member-str"></a>

idMember

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/membersVoted/{idMember}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.remove_sticker_by_ids`<a id="trellocardremove_sticker_by_ids"></a>

deleteCardsStickersByIdCardByIdSticker()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.remove_sticker_by_ids(
    id_card="idCard_example",
    id_sticker="idSticker_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_sticker: `str`<a id="id_sticker-str"></a>

idSticker

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/stickers/{idSticker}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_action_comment_by_id_card_by_id_action`<a id="trellocardupdate_action_comment_by_id_card_by_id_action"></a>

This can only be done by the original author of the comment.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_action_comment_by_id_card_by_id_action(
    id_card="idCard_example",
    id_action="idAction_example",
    text="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_action: `str`<a id="id_action-str"></a>

idAction

##### text: `str`<a id="text-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsActionsComments`](./trello_python_sdk/type/cards_actions_comments.py)
Attributes of \"Cards Actions Comments\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/actions/{idAction}/comments` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_attachment_cover_by_id_card`<a id="trellocardupdate_attachment_cover_by_id_card"></a>

updateCardsIdAttachmentCoverByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_attachment_cover_by_id_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

Id of the image attachment of this card to use as its cover, or null for no cover

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdAttachmentCover`](./trello_python_sdk/type/cards_id_attachment_cover.py)
Attributes of \"Cards Id Attachment Cover\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idAttachmentCover` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_board_by_id_card`<a id="trellocardupdate_board_by_id_card"></a>

updateCardsIdBoardByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_board_by_id_card(
    id_card="idCard_example",
    id_list="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_list: `str`<a id="id_list-str"></a>

id of the list that the card should be moved to on the new board

##### value: `str`<a id="value-str"></a>

id of the board the card should be moved to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdBoard`](./trello_python_sdk/type/cards_id_board.py)
Attributes of \"Cards Id Board\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idBoard` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_by_id_card`<a id="trellocardupdate_by_id_card"></a>

updateCardsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_by_id_card(
    id_card="idCard_example",
    closed="string_example",
    desc="string_example",
    due="string_example",
    file_source="string_example",
    id_attachment_cover="string_example",
    id_board="string_example",
    id_card_source="string_example",
    id_labels="string_example",
    id_list="string_example",
    id_members="string_example",
    keep_from_source="string_example",
    labels="string_example",
    name="string_example",
    pos="string_example",
    subscribed="string_example",
    url_source="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### closed: `str`<a id="closed-str"></a>

 true or false

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### due: `str`<a id="due-str"></a>

A date, or null

##### file_source: `str`<a id="file_source-str"></a>

A file

##### id_attachment_cover: `str`<a id="id_attachment_cover-str"></a>

Id of the image attachment of this card to use as its cover, or null for no cover

##### id_board: `str`<a id="id_board-str"></a>

id of the board the card should be moved to

##### id_card_source: `str`<a id="id_card_source-str"></a>

The id of the card to copy into a new card.

##### id_labels: `str`<a id="id_labels-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### id_list: `str`<a id="id_list-str"></a>

id of the list that the card should be added to

##### id_members: `str`<a id="id_members-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### keep_from_source: `str`<a id="keep_from_source-str"></a>

Properties of the card to copy over from the source.

##### labels: `str`<a id="labels-str"></a>

all or a comma-separated list of: blue, green, orange, purple, red or yellow

##### name: `str`<a id="name-str"></a>

The name of the new card.  It isn&#39;t required if the name is being copied from provided by a URL, file or card that is being copied.

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

##### url_source: `str`<a id="url_source-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Cards`](./trello_python_sdk/type/cards.py)
Attributes of \"Cards\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_check_item_pos_by_id`<a id="trellocardupdate_check_item_pos_by_id"></a>

updateCardsChecklistCheckItemPosByIdCardByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_check_item_pos_by_id(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklistCheckItemPos`](./trello_python_sdk/type/cards_checklist_check_item_pos.py)
Attributes of \"Cards Checklist Check Item Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_checklist_check_item`<a id="trellocardupdate_checklist_check_item"></a>

updateCardsChecklistCheckItemByIdCardByIdChecklistCurrentByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_checklist_check_item(
    id_card="idCard_example",
    id_checklist_current="idChecklistCurrent_example",
    id_check_item="idCheckItem_example",
    id_checklist="string_example",
    name="string_example",
    pos="string_example",
    state="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist_current: `str`<a id="id_checklist_current-str"></a>

idChecklistCurrent

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

##### id_checklist: `str`<a id="id_checklist-str"></a>

An id, or null

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### state: `str`<a id="state-str"></a>

One of: complete, false, incomplete or true

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklistIdChecklistCurrentCheckItem`](./trello_python_sdk/type/cards_checklist_id_checklist_current_check_item.py)
Attributes of \"Cards Checklist Id Checklist Current Check Item\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklistCurrent}/checkItem/{idCheckItem}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_checklist_check_item_name_by_id`<a id="trellocardupdate_checklist_check_item_name_by_id"></a>

updateCardsChecklistCheckItemNameByIdCardByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_checklist_check_item_name_by_id(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklistCheckItemName`](./trello_python_sdk/type/cards_checklist_check_item_name.py)
Attributes of \"Cards Checklist Check Item Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_checklist_check_item_state`<a id="trellocardupdate_checklist_check_item_state"></a>

updateCardsChecklistCheckItemStateByIdCardByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_checklist_check_item_state(
    id_card="idCard_example",
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

##### value: `str`<a id="value-str"></a>

One of: complete, false, incomplete or true

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsChecklistCheckItemState`](./trello_python_sdk/type/cards_checklist_check_item_state.py)
Attributes of \"Cards Checklist Check Item State\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/checklist/{idChecklist}/checkItem/{idCheckItem}/state` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_closed_by_id`<a id="trellocardupdate_closed_by_id"></a>

updateCardsClosedByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_closed_by_id(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsClosed`](./trello_python_sdk/type/cards_closed.py)
Attributes of \"Cards Closed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/closed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_description_by_id_card`<a id="trellocardupdate_description_by_id_card"></a>

updateCardsDescByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_description_by_id_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsDesc`](./trello_python_sdk/type/cards_desc.py)
Attributes of \"Cards Desc\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/desc` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_due_by_id`<a id="trellocardupdate_due_by_id"></a>

updateCardsDueByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_due_by_id(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

A date, or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsDue`](./trello_python_sdk/type/cards_due.py)
Attributes of \"Cards Due\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/due` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_id_list_by_id_card`<a id="trellocardupdate_id_list_by_id_card"></a>

updateCardsIdListByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_id_list_by_id_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

id of the list the card should be moved to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdList`](./trello_python_sdk/type/cards_id_list.py)
Attributes of \"Cards Id List\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idList` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_id_members`<a id="trellocardupdate_id_members"></a>

updateCardsIdMembersByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_id_members(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

The id of the member to add to the card

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsIdMembers`](./trello_python_sdk/type/cards_id_members.py)
Attributes of \"Cards Id Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/idMembers` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_labels`<a id="trellocardupdate_labels"></a>

updateCardsLabelsByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_labels(
    id_card="idCard_example",
    color="string_example",
    name="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### color: `str`<a id="color-str"></a>

A valid label color or null

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### value: `str`<a id="value-str"></a>

all or a comma-separated list of: blue, green, orange, purple, red or yellow

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsLabels`](./trello_python_sdk/type/cards_labels.py)
Attributes of \"Cards Labels\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/labels` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_name_by_id`<a id="trellocardupdate_name_by_id"></a>

updateCardsNameByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_name_by_id(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsName`](./trello_python_sdk/type/cards_name.py)
Attributes of \"Cards Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_pos_by_id_card`<a id="trellocardupdate_pos_by_id_card"></a>

updateCardsPosByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_pos_by_id_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsPos`](./trello_python_sdk/type/cards_pos.py)
Attributes of \"Cards Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_stickers_by_id_card_by_id_sticker`<a id="trellocardupdate_stickers_by_id_card_by_id_sticker"></a>

updateCardsStickersByIdCardByIdSticker()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_stickers_by_id_card_by_id_sticker(
    id_card="idCard_example",
    id_sticker="idSticker_example",
    image="string_example",
    left="string_example",
    rotate="string_example",
    top="string_example",
    z_index="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### id_sticker: `str`<a id="id_sticker-str"></a>

idSticker

##### image: `str`<a id="image-str"></a>

a string with a length from 0 to 16384

##### left: `str`<a id="left-str"></a>

undefined

##### rotate: `str`<a id="rotate-str"></a>

undefined

##### top: `str`<a id="top-str"></a>

undefined

##### z_index: `str`<a id="z_index-str"></a>

Valid Z values for stickers, must be an integer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsStickers`](./trello_python_sdk/type/cards_stickers.py)
Attributes of \"Cards Stickers\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/stickers/{idSticker}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.card.update_subscribed_by_id_card`<a id="trellocardupdate_subscribed_by_id_card"></a>

updateCardsSubscribedByIdCard()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.card.update_subscribed_by_id_card(
    id_card="idCard_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_card: `str`<a id="id_card-str"></a>

card id or shortlink

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CardsSubscribed`](./trello_python_sdk/type/cards_subscribed.py)
Attributes of \"Cards Subscribed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/cards/{idCard}/subscribed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.add_check_items_by_id_checklist`<a id="trellochecklistadd_check_items_by_id_checklist"></a>

addChecklistsCheckItemsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.add_check_items_by_id_checklist(
    id_checklist="idChecklist_example",
    checked="string_example",
    name="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### checked: `str`<a id="checked-str"></a>

 true or false

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChecklistsCheckItems`](./trello_python_sdk/type/checklists_check_items.py)
Attributes of \"Checklists Check Items\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/checkItems` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.create`<a id="trellochecklistcreate"></a>

addChecklists()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.create(
    id_board="string_example",
    id_card="string_example",
    id_checklist_source="string_example",
    name="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

id of the board that the checklist should be added to

##### id_card: `str`<a id="id_card-str"></a>

id of the card that the checklist should be added to

##### id_checklist_source: `str`<a id="id_checklist_source-str"></a>

The id of the source checklist to copy into a new checklist.

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Checklists`](./trello_python_sdk/type/checklists.py)
Attributes of \"Checklists\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_board_by_id_checklist`<a id="trellochecklistget_board_by_id_checklist"></a>

getChecklistsBoardByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_board_by_id_checklist(
    id_checklist="idChecklist_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_board_by_id_checklist_by_field`<a id="trellochecklistget_board_by_id_checklist_by_field"></a>

getChecklistsBoardByIdChecklistByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_board_by_id_checklist_by_field(
    id_checklist="idChecklist_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_by_id`<a id="trellochecklistget_by_id"></a>

getChecklistsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_by_id(
    id_checklist="idChecklist_example",
    cards="none",
    card_fields="all",
    check_items="all",
    check_item_fields="name, nameData, pos and state",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### check_items: `str`<a id="check_items-str"></a>

One of: all or none

##### check_item_fields: `str`<a id="check_item_fields-str"></a>

all or a comma-separated list of: name, nameData, pos, state or type

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: idBoard, idCard, name or pos

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_by_id_field`<a id="trellochecklistget_by_id_field"></a>

getChecklistsByIdChecklistByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_by_id_field(
    id_checklist="idChecklist_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_cards_by_filter`<a id="trellochecklistget_cards_by_filter"></a>

getChecklistsCardsByIdChecklistByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_cards_by_filter(
    id_checklist="idChecklist_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/cards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_check_items_by_id_checklist`<a id="trellochecklistget_check_items_by_id_checklist"></a>

getChecklistsCheckItemsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_check_items_by_id_checklist(
    id_checklist="idChecklist_example",
    filter="all",
    fields="name, nameData, pos and state",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### filter: `str`<a id="filter-str"></a>

One of: all or none

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: name, nameData, pos, state or type

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/checkItems` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.get_check_items_by_id_checklist_by_id_check_item`<a id="trellochecklistget_check_items_by_id_checklist_by_id_check_item"></a>

getChecklistsCheckItemsByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.get_check_items_by_id_checklist_by_id_check_item(
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
    fields="name, nameData, pos and state",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: name, nameData, pos, state or type

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/checkItems/{idCheckItem}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.list_cards_by_id_checklist`<a id="trellochecklistlist_cards_by_id_checklist"></a>

getChecklistsCardsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.list_cards_by_id_checklist(
    id_checklist="idChecklist_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    stickers="string_example",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    limit="string_example",
    since="string_example",
    before="string_example",
    filter="open",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### stickers: `str`<a id="stickers-str"></a>

 true or false

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 1000

##### since: `str`<a id="since-str"></a>

A date, or null

##### before: `str`<a id="before-str"></a>

A date, or null

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none or open

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.remove_by_id`<a id="trellochecklistremove_by_id"></a>

deleteChecklistsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.remove_by_id(
    id_checklist="idChecklist_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.remove_by_id_check_item`<a id="trellochecklistremove_by_id_check_item"></a>

deleteChecklistsCheckItemsByIdChecklistByIdCheckItem()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.remove_by_id_check_item(
    id_checklist="idChecklist_example",
    id_check_item="idCheckItem_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_check_item: `str`<a id="id_check_item-str"></a>

idCheckItem

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/checkItems/{idCheckItem}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.update_by_id_checklist`<a id="trellochecklistupdate_by_id_checklist"></a>

updateChecklistsByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.update_by_id_checklist(
    id_checklist="idChecklist_example",
    id_board="string_example",
    id_card="string_example",
    id_checklist_source="string_example",
    name="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### id_board: `str`<a id="id_board-str"></a>

id of the board that the checklist should be added to

##### id_card: `str`<a id="id_card-str"></a>

id of the card that the checklist should be added to

##### id_checklist_source: `str`<a id="id_checklist_source-str"></a>

The id of the source checklist to copy into a new checklist.

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Checklists`](./trello_python_sdk/type/checklists.py)
Attributes of \"Checklists\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.update_id_card_by_id_checklist`<a id="trellochecklistupdate_id_card_by_id_checklist"></a>

updateChecklistsIdCardByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.update_id_card_by_id_checklist(
    id_checklist="idChecklist_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### value: `str`<a id="value-str"></a>

The id of the card that the checklist is on

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChecklistsIdCard`](./trello_python_sdk/type/checklists_id_card.py)
Attributes of \"Checklists Id Card\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/idCard` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.update_name_by_id_checklist`<a id="trellochecklistupdate_name_by_id_checklist"></a>

updateChecklistsNameByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.update_name_by_id_checklist(
    id_checklist="idChecklist_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChecklistsName`](./trello_python_sdk/type/checklists_name.py)
Attributes of \"Checklists Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.checklist.update_pos_by_id_checklist`<a id="trellochecklistupdate_pos_by_id_checklist"></a>

updateChecklistsPosByIdChecklist()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.checklist.update_pos_by_id_checklist(
    id_checklist="idChecklist_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_checklist: `str`<a id="id_checklist-str"></a>

idChecklist

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChecklistsPos`](./trello_python_sdk/type/checklists_pos.py)
Attributes of \"Checklists Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/checklists/{idChecklist}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.create_labels`<a id="trellolabelcreate_labels"></a>

addLabels()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.create_labels(
    color="string_example",
    id_board="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### color: `str`<a id="color-str"></a>

A valid label color or null

##### id_board: `str`<a id="id_board-str"></a>

An id

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Labels`](./trello_python_sdk/type/labels.py)
Attributes of \"Labels\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.get_board_by_id_label`<a id="trellolabelget_board_by_id_label"></a>

getLabelsBoardByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.get_board_by_id_label(
    id_label="idLabel_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.get_board_by_id_label_by_field`<a id="trellolabelget_board_by_id_label_by_field"></a>

getLabelsBoardByIdLabelByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.get_board_by_id_label_by_field(
    id_label="idLabel_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.get_by_id_label`<a id="trellolabelget_by_id_label"></a>

getLabelsByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.get_by_id_label(
    id_label="idLabel_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: color, idBoard, name or uses

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.remove_by_id_label`<a id="trellolabelremove_by_id_label"></a>

deleteLabelsByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.remove_by_id_label(
    id_label="idLabel_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.update_by_id_label`<a id="trellolabelupdate_by_id_label"></a>

updateLabelsByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.update_by_id_label(
    id_label="idLabel_example",
    color="string_example",
    id_board="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### color: `str`<a id="color-str"></a>

A valid label color or null

##### id_board: `str`<a id="id_board-str"></a>

An id

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Labels`](./trello_python_sdk/type/labels.py)
Attributes of \"Labels\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.update_color_by_id_label`<a id="trellolabelupdate_color_by_id_label"></a>

updateLabelsColorByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.update_color_by_id_label(
    id_label="idLabel_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### value: `str`<a id="value-str"></a>

A valid label color or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelsColor`](./trello_python_sdk/type/labels_color.py)
Attributes of \"Labels Color\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}/color` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.label.update_name_by_id_label`<a id="trellolabelupdate_name_by_id_label"></a>

updateLabelsNameByIdLabel()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.label.update_name_by_id_label(
    id_label="idLabel_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_label: `str`<a id="id_label-str"></a>

idLabel

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`LabelsName`](./trello_python_sdk/type/labels_name.py)
Attributes of \"Labels Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/labels/{idLabel}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.archive_all_cards_by_id_list`<a id="trellolistarchive_all_cards_by_id_list"></a>

addListsArchiveAllCardsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.archive_all_cards_by_id_list(
    id_list="idList_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/archiveAllCards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.create_cards_by_id_list`<a id="trellolistcreate_cards_by_id_list"></a>

addListsCardsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.create_cards_by_id_list(
    id_list="idList_example",
    desc="string_example",
    due="string_example",
    id_members="string_example",
    labels="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### due: `str`<a id="due-str"></a>

A date, or null

##### id_members: `str`<a id="id_members-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### labels: `str`<a id="labels-str"></a>

all or a comma-separated list of: blue, green, orange, purple, red or yellow

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsCards`](./trello_python_sdk/type/lists_cards.py)
Attributes of \"Lists Cards\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/cards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.create_list`<a id="trellolistcreate_list"></a>

addLists()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.create_list(
    closed="string_example",
    id_board="string_example",
    id_list_source="string_example",
    name="string_example",
    pos="string_example",
    subscribed="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### closed: `str`<a id="closed-str"></a>

 true or false

##### id_board: `str`<a id="id_board-str"></a>

id of the board that the list should be added to

##### id_list_source: `str`<a id="id_list_source-str"></a>

The id of the list to copy into a new list.

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Lists`](./trello_python_sdk/type/lists.py)
Attributes of \"Lists\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_actions_by_id_list`<a id="trellolistget_actions_by_id_list"></a>

getListsActionsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_actions_by_id_list(
    id_list="idList_example",
    entities="string_example",
    display="string_example",
    filter="all",
    fields="all",
    limit="50",
    format="list",
    since="string_example",
    before="string_example",
    page="0",
    id_models="string_example",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

##### format: `str`<a id="format-str"></a>

One of: count, list or minimal

##### since: `str`<a id="since-str"></a>

A date, null or lastView

##### before: `str`<a id="before-str"></a>

A date, or null

##### page: `str`<a id="page-str"></a>

Page * limit must be less than 1000

##### id_models: `str`<a id="id_models-str"></a>

Only return actions related to these model ids

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_board_by_id_list_by_field`<a id="trellolistget_board_by_id_list_by_field"></a>

getListsBoardByIdListByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_board_by_id_list_by_field(
    id_list="idList_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_by_id_list`<a id="trellolistget_by_id_list"></a>

getListsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_by_id_list(
    id_list="idList_example",
    cards="none",
    card_fields="all",
    board="string_example",
    board_fields="name, desc, descData, closed, idOrganization, pinned, url and prefs",
    fields="name, closed, idBoard and pos",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none or open

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### board: `str`<a id="board-str"></a>

 true or false

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_by_id_list_by_field`<a id="trellolistget_by_id_list_by_field"></a>

getListsByIdListByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_by_id_list_by_field(
    id_list="idList_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_cards_by_filter`<a id="trellolistget_cards_by_filter"></a>

getListsCardsByIdListByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_cards_by_filter(
    id_list="idList_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/cards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.get_cards_by_id_list`<a id="trellolistget_cards_by_id_list"></a>

getListsCardsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.get_cards_by_id_list(
    id_list="idList_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    stickers="string_example",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    limit="string_example",
    since="string_example",
    before="string_example",
    filter="open",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### stickers: `str`<a id="stickers-str"></a>

 true or false

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 1000

##### since: `str`<a id="since-str"></a>

A date, or null

##### before: `str`<a id="before-str"></a>

A date, or null

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none or open

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.id_board_get`<a id="trellolistid_board_get"></a>

getListsBoardByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.id_board_get(
    id_list="idList_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.move_all_cards_by_id_list`<a id="trellolistmove_all_cards_by_id_list"></a>

addListsMoveAllCardsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.move_all_cards_by_id_list(
    id_list="idList_example",
    id_board="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### id_board: `str`<a id="id_board-str"></a>

id of the board that the cards should be moved to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsMoveAllCards`](./trello_python_sdk/type/lists_move_all_cards.py)
Attributes of \"Lists Move All Cards\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/moveAllCards` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_by_id_list`<a id="trellolistupdate_by_id_list"></a>

updateListsByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_by_id_list(
    id_list="idList_example",
    closed="string_example",
    id_board="string_example",
    id_list_source="string_example",
    name="string_example",
    pos="string_example",
    subscribed="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### closed: `str`<a id="closed-str"></a>

 true or false

##### id_board: `str`<a id="id_board-str"></a>

id of the board that the list should be added to

##### id_list_source: `str`<a id="id_list_source-str"></a>

The id of the list to copy into a new list.

##### name: `str`<a id="name-str"></a>

a string with a length from 1 to 16384

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### subscribed: `str`<a id="subscribed-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Lists`](./trello_python_sdk/type/lists.py)
Attributes of \"Lists\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_closed_by_id_list`<a id="trellolistupdate_closed_by_id_list"></a>

updateListsClosedByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_closed_by_id_list(
    id_list="idList_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsClosed`](./trello_python_sdk/type/lists_closed.py)
Attributes of \"Lists Closed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/closed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_id_board_by_id_list`<a id="trellolistupdate_id_board_by_id_list"></a>

updateListsIdBoardByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_id_board_by_id_list(
    id_list="idList_example",
    pos="string_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### pos: `str`<a id="pos-str"></a>

position of the list on the new board

##### value: `str`<a id="value-str"></a>

id of the board the list should be moved to

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsIdBoard`](./trello_python_sdk/type/lists_id_board.py)
Attributes of \"Lists Id Board\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/idBoard` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_name_by_id_list`<a id="trellolistupdate_name_by_id_list"></a>

updateListsNameByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_name_by_id_list(
    id_list="idList_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsName`](./trello_python_sdk/type/lists_name.py)
Attributes of \"Lists Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_pos_by_id_list`<a id="trellolistupdate_pos_by_id_list"></a>

updateListsPosByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_pos_by_id_list(
    id_list="idList_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsPos`](./trello_python_sdk/type/lists_pos.py)
Attributes of \"Lists Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.list.update_subscribed_by_id_list`<a id="trellolistupdate_subscribed_by_id_list"></a>

updateListsSubscribedByIdList()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.list.update_subscribed_by_id_list(
    id_list="idList_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_list: `str`<a id="id_list-str"></a>

idList

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ListsSubscribed`](./trello_python_sdk/type/lists_subscribed.py)
Attributes of \"Lists Subscribed\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/lists/{idList}/subscribed` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_board_backgrounds`<a id="trellomemberadd_board_backgrounds"></a>

addMembersBoardBackgroundsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_board_backgrounds(
    id_member="idMember_example",
    brightness="string_example",
    file="string_example",
    tile="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### brightness: `str`<a id="brightness-str"></a>

One of: dark, light or unknown

##### file: `str`<a id="file-str"></a>

A file

##### tile: `str`<a id="tile-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardBackgrounds`](./trello_python_sdk/type/members_board_backgrounds.py)
Attributes of \"Members Board Backgrounds\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardBackgrounds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_board_stars_by_id_member`<a id="trellomemberadd_board_stars_by_id_member"></a>

addMembersBoardStarsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_board_stars_by_id_member(
    id_member="idMember_example",
    id_board="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board: `str`<a id="id_board-str"></a>

The id of the board to star

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardStars`](./trello_python_sdk/type/members_board_stars.py)
Attributes of \"Members Board Stars\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_custom_board_backgrounds`<a id="trellomemberadd_custom_board_backgrounds"></a>

addMembersCustomBoardBackgroundsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_custom_board_backgrounds(
    id_member="idMember_example",
    brightness="string_example",
    file="string_example",
    tile="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### brightness: `str`<a id="brightness-str"></a>

One of: dark, light or unknown

##### file: `str`<a id="file-str"></a>

A file

##### tile: `str`<a id="tile-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersCustomBoardBackgrounds`](./trello_python_sdk/type/members_custom_board_backgrounds.py)
Attributes of \"Members Custom Board Backgrounds\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customBoardBackgrounds` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_custom_emoji_by_id_member`<a id="trellomemberadd_custom_emoji_by_id_member"></a>

addMembersCustomEmojiByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_custom_emoji_by_id_member(
    id_member="idMember_example",
    file="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### file: `str`<a id="file-str"></a>

A file

##### name: `str`<a id="name-str"></a>

a string with a length from 2 to 64

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersCustomEmoji`](./trello_python_sdk/type/members_custom_emoji.py)
Attributes of \"Members Custom Emoji\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customEmoji` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_custom_stickers`<a id="trellomemberadd_custom_stickers"></a>

addMembersCustomStickersByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_custom_stickers(
    id_member="idMember_example",
    file="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### file: `str`<a id="file-str"></a>

A file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersCustomStickers`](./trello_python_sdk/type/members_custom_stickers.py)
Attributes of \"Members Custom Stickers\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customStickers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.add_one_time_messages_dismissed_by_id_member`<a id="trellomemberadd_one_time_messages_dismissed_by_id_member"></a>

addMembersOneTimeMessagesDismissedByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.add_one_time_messages_dismissed_by_id_member(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

Type of message dismissed

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersOneTimeMessagesDismissed`](./trello_python_sdk/type/members_one_time_messages_dismissed.py)
Attributes of \"Members One Time Messages Dismissed\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/oneTimeMessagesDismissed` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.create_saved_search`<a id="trellomembercreate_saved_search"></a>

addMembersSavedSearchesByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.create_saved_search(
    id_member="idMember_example",
    name="string_example",
    pos="string_example",
    query="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### name: `str`<a id="name-str"></a>

A non-empty string with at least one non-space character

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### query: `str`<a id="query-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersSavedSearches`](./trello_python_sdk/type/members_saved_searches.py)
Attributes of \"Members Saved Searches\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.delete_board_background`<a id="trellomemberdelete_board_background"></a>

deleteMembersBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.delete_board_background(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardBackgrounds/{idBoardBackground}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_board_background_by_ids`<a id="trellomemberget_board_background_by_ids"></a>

getMembersBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_board_background_by_ids(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardBackgrounds/{idBoardBackground}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_board_backgrounds_by_id`<a id="trellomemberget_board_backgrounds_by_id"></a>

getMembersBoardBackgroundsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_board_backgrounds_by_id(
    id_member="idMember_example",
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all, custom, default, none or premium

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardBackgrounds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_board_star_by_id_member`<a id="trellomemberget_board_star_by_id_member"></a>

getMembersBoardStarsByIdMemberByIdBoardStar()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_board_star_by_id_member(
    id_member="idMember_example",
    id_board_star="idBoardStar_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_star: `str`<a id="id_board_star-str"></a>

idBoardStar

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars/{idBoardStar}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_board_stars_by_id`<a id="trellomemberget_board_stars_by_id"></a>

getMembersBoardStarsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_board_stars_by_id(
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_boards`<a id="trellomemberget_boards"></a>

getMembersBoardsByIdMemberByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_boards(
    id_member="idMember_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_boards_by_id_member`<a id="trellomemberget_boards_by_id_member"></a>

getMembersBoardsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_boards_by_id_member(
    id_member="idMember_example",
    filter="all",
    fields="all",
    actions="string_example",
    actions_entities="string_example",
    actions_limit="50",
    actions_format="list",
    actions_since="string_example",
    action_fields="all",
    memberships="none",
    organization="string_example",
    organization_fields="name and displayName",
    lists="none",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### actions_format: `str`<a id="actions_format-str"></a>

One of: count, list or minimal

##### actions_since: `str`<a id="actions_since-str"></a>

A date, null or lastView

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### memberships: `str`<a id="memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### organization: `str`<a id="organization-str"></a>

 true or false

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### lists: `str`<a id="lists-str"></a>

One of: all, closed, none or open

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_boards_invited_by_id_member_by_field`<a id="trellomemberget_boards_invited_by_id_member_by_field"></a>

getMembersBoardsInvitedByIdMemberByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_boards_invited_by_id_member_by_field(
    id_member="idMember_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardsInvited/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_by_field`<a id="trellomemberget_by_field"></a>

getMembersByIdMemberByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_by_field(
    id_member="idMember_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_by_id`<a id="trellomemberget_by_id"></a>

If you specify 'me' as the username, this call will respond as if you had supplied the username associated with the supplied token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_by_id(
    id_member="idMember_example",
    actions="string_example",
    actions_entities="string_example",
    actions_display="string_example",
    actions_limit="50",
    action_fields="all",
    action_since="string_example",
    action_before="string_example",
    cards="none",
    card_fields="all",
    card_members="string_example",
    card_member_fields="avatarHash, fullName, initials and username",
    card_attachments="string_example",
    card_attachment_fields="url and previews",
    card_stickers="string_example",
    boards="string_example",
    board_fields="name, closed, idOrganization and pinned",
    board_actions="string_example",
    board_actions_entities="string_example",
    board_actions_display="string_example",
    board_actions_format="list",
    board_actions_since="string_example",
    board_actions_limit="50",
    board_action_fields="all",
    board_lists="none",
    board_memberships="none",
    board_organization="string_example",
    board_organization_fields="name and displayName",
    boards_invited="string_example",
    boards_invited_fields="name, closed, idOrganization and pinned",
    board_stars="string_example",
    saved_searches="string_example",
    organizations="none",
    organization_fields="all",
    organization_paid_account="string_example",
    organizations_invited="none",
    organizations_invited_fields="all",
    notifications="string_example",
    notifications_entities="string_example",
    notifications_display="string_example",
    notifications_limit="50",
    notification_fields="all",
    notification_member_creator="string_example",
    notification_member_creator_fields="avatarHash, fullName, initials and username",
    notification_before="string_example",
    notification_since="string_example",
    tokens="none",
    paid_account="string_example",
    board_backgrounds="none",
    custom_board_backgrounds="none",
    custom_stickers="none",
    custom_emoji="none",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_display: `str`<a id="actions_display-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### action_since: `str`<a id="action_since-str"></a>

A date, null or lastView

##### action_before: `str`<a id="action_before-str"></a>

A date, or null

##### cards: `str`<a id="cards-str"></a>

One of: all, closed, none, open or visible

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### card_members: `str`<a id="card_members-str"></a>

 true or false

##### card_member_fields: `str`<a id="card_member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### card_attachments: `str`<a id="card_attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### card_attachment_fields: `str`<a id="card_attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### card_stickers: `str`<a id="card_stickers-str"></a>

 true or false

##### boards: `str`<a id="boards-str"></a>

all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### board_actions: `str`<a id="board_actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### board_actions_entities: `str`<a id="board_actions_entities-str"></a>

 true or false

##### board_actions_display: `str`<a id="board_actions_display-str"></a>

 true or false

##### board_actions_format: `str`<a id="board_actions_format-str"></a>

One of: count, list or minimal

##### board_actions_since: `str`<a id="board_actions_since-str"></a>

A date, null or lastView

##### board_actions_limit: `str`<a id="board_actions_limit-str"></a>

a number from 0 to 1000

##### board_action_fields: `str`<a id="board_action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### board_lists: `str`<a id="board_lists-str"></a>

One of: all, closed, none or open

##### board_memberships: `str`<a id="board_memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### board_organization: `str`<a id="board_organization-str"></a>

 true or false

##### board_organization_fields: `str`<a id="board_organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### boards_invited: `str`<a id="boards_invited-str"></a>

all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned

##### boards_invited_fields: `str`<a id="boards_invited_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### board_stars: `str`<a id="board_stars-str"></a>

 true or false

##### saved_searches: `str`<a id="saved_searches-str"></a>

 true or false

##### organizations: `str`<a id="organizations-str"></a>

One of: all, members, none or public

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### organization_paid_account: `str`<a id="organization_paid_account-str"></a>

 true or false

##### organizations_invited: `str`<a id="organizations_invited-str"></a>

One of: all, members, none or public

##### organizations_invited_fields: `str`<a id="organizations_invited_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### notifications: `str`<a id="notifications-str"></a>

all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard

##### notifications_entities: `str`<a id="notifications_entities-str"></a>

 true or false

##### notifications_display: `str`<a id="notifications_display-str"></a>

 true or false

##### notifications_limit: `str`<a id="notifications_limit-str"></a>

a number from 1 to 1000

##### notification_fields: `str`<a id="notification_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator, type or unread

##### notification_member_creator: `str`<a id="notification_member_creator-str"></a>

 true or false

##### notification_member_creator_fields: `str`<a id="notification_member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### notification_before: `str`<a id="notification_before-str"></a>

An id, or null

##### notification_since: `str`<a id="notification_since-str"></a>

An id, or null

##### tokens: `str`<a id="tokens-str"></a>

One of: all or none

##### paid_account: `str`<a id="paid_account-str"></a>

 true or false

##### board_backgrounds: `str`<a id="board_backgrounds-str"></a>

One of: all, custom, default, none or premium

##### custom_board_backgrounds: `str`<a id="custom_board_backgrounds-str"></a>

One of: all or none

##### custom_stickers: `str`<a id="custom_stickers-str"></a>

One of: all or none

##### custom_emoji: `str`<a id="custom_emoji-str"></a>

One of: all or none

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_cards_by_filter`<a id="trellomemberget_cards_by_filter"></a>

getMembersCardsByIdMemberByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_cards_by_filter(
    id_member="idMember_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/cards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_cards_by_id_member`<a id="trellomemberget_cards_by_id_member"></a>

getMembersCardsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_cards_by_id_member(
    id_member="idMember_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    stickers="string_example",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    limit="string_example",
    since="string_example",
    before="string_example",
    filter="visible",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### stickers: `str`<a id="stickers-str"></a>

 true or false

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 1000

##### since: `str`<a id="since-str"></a>

A date, or null

##### before: `str`<a id="before-str"></a>

A date, or null

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none, open or visible

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_custom_board_background_by_ids`<a id="trellomemberget_custom_board_background_by_ids"></a>

getMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_custom_board_background_by_ids(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: brightness, fullSizeUrl, scaled or tile

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customBoardBackgrounds/{idBoardBackground}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_custom_board_backgrounds_by_id`<a id="trellomemberget_custom_board_backgrounds_by_id"></a>

getMembersCustomBoardBackgroundsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_custom_board_backgrounds_by_id(
    id_member="idMember_example",
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all or none

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customBoardBackgrounds` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_custom_emoji_by_ids`<a id="trellomemberget_custom_emoji_by_ids"></a>

getMembersCustomEmojiByIdMemberByIdCustomEmoji()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_custom_emoji_by_ids(
    id_member="idMember_example",
    id_custom_emoji="idCustomEmoji_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_custom_emoji: `str`<a id="id_custom_emoji-str"></a>

idCustomEmoji

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: name or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customEmoji/{idCustomEmoji}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_custom_sticker_by_ids`<a id="trellomemberget_custom_sticker_by_ids"></a>

getMembersCustomStickersByIdMemberByIdCustomSticker()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_custom_sticker_by_ids(
    id_member="idMember_example",
    id_custom_sticker="idCustomSticker_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_custom_sticker: `str`<a id="id_custom_sticker-str"></a>

idCustomSticker

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: scaled or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customStickers/{idCustomSticker}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_custom_stickers_by_id_member`<a id="trellomemberget_custom_stickers_by_id_member"></a>

This gets a list of all of the user’s uploaded stickers

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_custom_stickers_by_id_member(
    id_member="idMember_example",
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all or none

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customStickers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_deltas_by_id_member`<a id="trellomemberget_deltas_by_id_member"></a>

getMembersDeltasByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_deltas_by_id_member(
    id_member="idMember_example",
    tags="tags_example",
    ix_last_update="ixLastUpdate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### tags: `str`<a id="tags-str"></a>

A valid tag for subscribing

##### ix_last_update: `str`<a id="ix_last_update-str"></a>

a number from -1 to Infinity

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/deltas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_invited_boards`<a id="trellomemberget_invited_boards"></a>

getMembersBoardsInvitedByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_invited_boards(
    id_member="idMember_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardsInvited` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_notifications_by_id_member`<a id="trellomemberget_notifications_by_id_member"></a>

You can only read the notifications for the member associated with the supplied token

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_notifications_by_id_member(
    id_member="idMember_example",
    entities="string_example",
    display="string_example",
    filter="all",
    read_filter="all",
    fields="all",
    limit="50",
    page="0",
    before="string_example",
    since="string_example",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAdminToBoard, addAdminToOrganization, addedAttachmentToCard, addedMemberToCard, addedToBoard, addedToCard, addedToOrganization, cardDueSoon, changeCard, closeBoard, commentCard, createdCard, declinedInvitationToBoard, declinedInvitationToOrganization, invitedToBoard, invitedToOrganization, makeAdminOfBoard, makeAdminOfOrganization, memberJoinedTrello, mentionedOnCard, removedFromBoard, removedFromCard, removedFromOrganization, removedMemberFromCard, unconfirmedInvitedToBoard, unconfirmedInvitedToOrganization or updateCheckItemStateOnCard

##### read_filter: `str`<a id="read_filter-str"></a>

One of: all, read or unread

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator, type or unread

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 1000

##### page: `str`<a id="page-str"></a>

a number from 0 to 100

##### before: `str`<a id="before-str"></a>

An id, or null

##### since: `str`<a id="since-str"></a>

An id, or null

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/notifications` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_notifications_by_id_member_by_filter`<a id="trellomemberget_notifications_by_id_member_by_filter"></a>

getMembersNotificationsByIdMemberByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_notifications_by_id_member_by_filter(
    id_member="idMember_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/notifications/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_organizations`<a id="trellomemberget_organizations"></a>

getMembersOrganizationsByIdMemberByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_organizations(
    id_member="idMember_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/organizations/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_saved_search_by_ids`<a id="trellomemberget_saved_search_by_ids"></a>

getMembersSavedSearchesByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_saved_search_by_ids(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_saved_searches_by_id_member`<a id="trellomemberget_saved_searches_by_id_member"></a>

getMembersSavedSearchesByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_saved_searches_by_id_member(
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.get_tokens_by_id_member`<a id="trellomemberget_tokens_by_id_member"></a>

getMembersTokensByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.get_tokens_by_id_member(
    id_member="idMember_example",
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all or none

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/tokens` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.list_actions_by_id_member`<a id="trellomemberlist_actions_by_id_member"></a>

getMembersActionsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.list_actions_by_id_member(
    id_member="idMember_example",
    entities="string_example",
    display="string_example",
    filter="all",
    fields="all",
    limit="50",
    format="list",
    since="string_example",
    before="string_example",
    page="0",
    id_models="string_example",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

##### format: `str`<a id="format-str"></a>

One of: count, list or minimal

##### since: `str`<a id="since-str"></a>

A date, null or lastView

##### before: `str`<a id="before-str"></a>

A date, or null

##### page: `str`<a id="page-str"></a>

Page * limit must be less than 1000

##### id_models: `str`<a id="id_models-str"></a>

Only return actions related to these model ids

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.list_custom_emoji_by_id_member`<a id="trellomemberlist_custom_emoji_by_id_member"></a>

This gets the list of all of the user’s uploaded emoji

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.list_custom_emoji_by_id_member(
    id_member="idMember_example",
    filter="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all or none

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customEmoji` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.list_invited_organizations_by_id`<a id="trellomemberlist_invited_organizations_by_id"></a>

getMembersOrganizationsInvitedByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.list_invited_organizations_by_id(
    id_member="idMember_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/organizationsInvited` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.list_organizations_by_id`<a id="trellomemberlist_organizations_by_id"></a>

getMembersOrganizationsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.list_organizations_by_id(
    id_member="idMember_example",
    filter="all",
    fields="all",
    paid_account="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### filter: `str`<a id="filter-str"></a>

One of: all, members, none or public

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### paid_account: `str`<a id="paid_account-str"></a>

 true or false

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/organizations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.list_organizations_invited_by_id_member_by_field`<a id="trellomemberlist_organizations_invited_by_id_member_by_field"></a>

getMembersOrganizationsInvitedByIdMemberByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.list_organizations_invited_by_id_member_by_field(
    id_member="idMember_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/organizationsInvited/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.remove_board_star_by_id_member_by_id_board_star`<a id="trellomemberremove_board_star_by_id_member_by_id_board_star"></a>

deleteMembersBoardStarsByIdMemberByIdBoardStar()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.remove_board_star_by_id_member_by_id_board_star(
    id_member="idMember_example",
    id_board_star="idBoardStar_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_star: `str`<a id="id_board_star-str"></a>

idBoardStar

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars/{idBoardStar}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.remove_custom_board_background_by_id`<a id="trellomemberremove_custom_board_background_by_id"></a>

deleteMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.remove_custom_board_background_by_id(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customBoardBackgrounds/{idBoardBackground}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.remove_custom_sticker_by_ids`<a id="trellomemberremove_custom_sticker_by_ids"></a>

deleteMembersCustomStickersByIdMemberByIdCustomSticker()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.remove_custom_sticker_by_ids(
    id_member="idMember_example",
    id_custom_sticker="idCustomSticker_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_custom_sticker: `str`<a id="id_custom_sticker-str"></a>

idCustomSticker

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customStickers/{idCustomSticker}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.remove_saved_search_by_ids`<a id="trellomemberremove_saved_search_by_ids"></a>

deleteMembersSavedSearchesByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.remove_saved_search_by_ids(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_avatar_source`<a id="trellomemberupdate_avatar_source"></a>

updateMembersAvatarSourceByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_avatar_source(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

One of: gravatar, none or upload

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersAvatarSource`](./trello_python_sdk/type/members_avatar_source.py)
Attributes of \"Members Avatar Source\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/avatarSource` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_bio_by_id`<a id="trellomemberupdate_bio_by_id"></a>

updateMembersBioByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_bio_by_id(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBio`](./trello_python_sdk/type/members_bio.py)
Attributes of \"Members Bio\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/bio` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_board_backgrounds_by_id`<a id="trellomemberupdate_board_backgrounds_by_id"></a>

updateMembersBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_board_backgrounds_by_id(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
    brightness="string_example",
    file="string_example",
    tile="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

##### brightness: `str`<a id="brightness-str"></a>

One of: dark, light or unknown

##### file: `str`<a id="file-str"></a>

A file

##### tile: `str`<a id="tile-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardBackgrounds`](./trello_python_sdk/type/members_board_backgrounds.py)
Attributes of \"Members Board Backgrounds\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardBackgrounds/{idBoardBackground}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_board_star`<a id="trellomemberupdate_board_star"></a>

updateMembersBoardStarsByIdMemberByIdBoardStar()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_board_star(
    id_member="idMember_example",
    id_board_star="idBoardStar_example",
    id_board="string_example",
    pos="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_star: `str`<a id="id_board_star-str"></a>

idBoardStar

##### id_board: `str`<a id="id_board-str"></a>

The id of the board to star

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardStars`](./trello_python_sdk/type/members_board_stars.py)
Attributes of \"Members Board Stars\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars/{idBoardStar}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_board_star_pos_by_id_member_by_id_board_star`<a id="trellomemberupdate_board_star_pos_by_id_member_by_id_board_star"></a>

updateMembersBoardStarsPosByIdMemberByIdBoardStar()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_board_star_pos_by_id_member_by_id_board_star(
    id_member="idMember_example",
    id_board_star="idBoardStar_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_star: `str`<a id="id_board_star-str"></a>

idBoardStar

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardStarsPos`](./trello_python_sdk/type/members_board_stars_pos.py)
Attributes of \"Members Board Stars Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars/{idBoardStar}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_board_stars_id_board`<a id="trellomemberupdate_board_stars_id_board"></a>

updateMembersBoardStarsIdBoardByIdMemberByIdBoardStar()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_board_stars_id_board(
    id_member="idMember_example",
    id_board_star="idBoardStar_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_star: `str`<a id="id_board_star-str"></a>

idBoardStar

##### value: `str`<a id="value-str"></a>

An id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersBoardStarsIdBoard`](./trello_python_sdk/type/members_board_stars_id_board.py)
Attributes of \"Members Board Stars Id Board\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/boardStars/{idBoardStar}/idBoard` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_by_id_member`<a id="trellomemberupdate_by_id_member"></a>

updateMembersByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_by_id_member(
    id_member="idMember_example",
    avatar_source="string_example",
    bio="string_example",
    full_name="string_example",
    initials="string_example",
    prefs_color_blind="string_example",
    prefs_locale="string_example",
    prefs_minutes_between_summaries="string_example",
    username="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### avatar_source: `str`<a id="avatar_source-str"></a>

One of: gravatar, none or upload

##### bio: `str`<a id="bio-str"></a>

a string with a length from 0 to 16384

##### full_name: `str`<a id="full_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### initials: `str`<a id="initials-str"></a>

A string with a length from 1 to 4.  Cannot begin or end with a space

##### prefs_color_blind: `str`<a id="prefs_color_blind-str"></a>

 true or false

##### prefs_locale: `str`<a id="prefs_locale-str"></a>

a string with a length from 0 to 255

##### prefs_minutes_between_summaries: `str`<a id="prefs_minutes_between_summaries-str"></a>

-1 (disabled), 1 or 60

##### username: `str`<a id="username-str"></a>

A string with a length of at least 3.  Only lowercase letters, underscores, and numbers are allowed.  Must be unique.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Members`](./trello_python_sdk/type/members.py)
Attributes of \"Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_custom_board_backgrounds`<a id="trellomemberupdate_custom_board_backgrounds"></a>

updateMembersCustomBoardBackgroundsByIdMemberByIdBoardBackground()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_custom_board_backgrounds(
    id_member="idMember_example",
    id_board_background="idBoardBackground_example",
    brightness="string_example",
    file="string_example",
    tile="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_board_background: `str`<a id="id_board_background-str"></a>

idBoardBackground

##### brightness: `str`<a id="brightness-str"></a>

One of: dark, light or unknown

##### file: `str`<a id="file-str"></a>

A file

##### tile: `str`<a id="tile-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersCustomBoardBackgrounds`](./trello_python_sdk/type/members_custom_board_backgrounds.py)
Attributes of \"Members Custom Board Backgrounds\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/customBoardBackgrounds/{idBoardBackground}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_full_name`<a id="trellomemberupdate_full_name"></a>

updateMembersFullNameByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_full_name(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersFullName`](./trello_python_sdk/type/members_full_name.py)
Attributes of \"Members Full Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/fullName` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_initials_by_id_member`<a id="trellomemberupdate_initials_by_id_member"></a>

updateMembersInitialsByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_initials_by_id_member(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

A string with a length from 1 to 4.  Cannot begin or end with a space

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersInitials`](./trello_python_sdk/type/members_initials.py)
Attributes of \"Members Initials\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/initials` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_prefs_color_blind_by_id_member`<a id="trellomemberupdate_prefs_color_blind_by_id_member"></a>

updateMembersPrefsColorBlindByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_prefs_color_blind_by_id_member(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsColorBlind`](./trello_python_sdk/type/prefs_color_blind.py)
Attributes of \"Prefs Color Blind\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/prefs/colorBlind` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_prefs_locale_by_id_member`<a id="trellomemberupdate_prefs_locale_by_id_member"></a>

updateMembersPrefsLocaleByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_prefs_locale_by_id_member(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 255

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsLocale`](./trello_python_sdk/type/prefs_locale.py)
Attributes of \"Prefs Locale\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/prefs/locale` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_prefs_minutes_between_summaries_by_id`<a id="trellomemberupdate_prefs_minutes_between_summaries_by_id"></a>

updateMembersPrefsMinutesBetweenSummariesByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_prefs_minutes_between_summaries_by_id(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

-1 (disabled), 1 or 60

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsMinutesBetweenSummaries`](./trello_python_sdk/type/prefs_minutes_between_summaries.py)
Attributes of \"Prefs Minutes Between Summaries\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/prefs/minutesBetweenSummaries` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_saved_search_query_by_id_member_by_id_saved_search`<a id="trellomemberupdate_saved_search_query_by_id_member_by_id_saved_search"></a>

updateMembersSavedSearchesQueryByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_saved_search_query_by_id_member_by_id_saved_search(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

##### value: `str`<a id="value-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersSavedSearchesQuery`](./trello_python_sdk/type/members_saved_searches_query.py)
Attributes of \"Members Saved Searches Query\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}/query` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_saved_searches_by_id_member_by_id_saved_search`<a id="trellomemberupdate_saved_searches_by_id_member_by_id_saved_search"></a>

updateMembersSavedSearchesByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_saved_searches_by_id_member_by_id_saved_search(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
    name="string_example",
    pos="string_example",
    query="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

##### name: `str`<a id="name-str"></a>

A non-empty string with at least one non-space character

##### pos: `str`<a id="pos-str"></a>

A position. top , bottom , or a positive number.

##### query: `str`<a id="query-str"></a>

a string with a length from 1 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersSavedSearches`](./trello_python_sdk/type/members_saved_searches.py)
Attributes of \"Members Saved Searches\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_saved_searches_name_by_id_member_by_id_saved_search`<a id="trellomemberupdate_saved_searches_name_by_id_member_by_id_saved_search"></a>

updateMembersSavedSearchesNameByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_saved_searches_name_by_id_member_by_id_saved_search(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

##### value: `str`<a id="value-str"></a>

A non-empty string with at least one non-space character

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersSavedSearchesName`](./trello_python_sdk/type/members_saved_searches_name.py)
Attributes of \"Members Saved Searches Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_saved_searches_pos_by_id_member_by_id_saved_search`<a id="trellomemberupdate_saved_searches_pos_by_id_member_by_id_saved_search"></a>

updateMembersSavedSearchesPosByIdMemberByIdSavedSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_saved_searches_pos_by_id_member_by_id_saved_search(
    id_member="idMember_example",
    id_saved_search="idSavedSearch_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### id_saved_search: `str`<a id="id_saved_search-str"></a>

idSavedSearch

##### value: `str`<a id="value-str"></a>

A position. top , bottom , or a positive number.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersSavedSearchesPos`](./trello_python_sdk/type/members_saved_searches_pos.py)
Attributes of \"Members Saved Searches Pos\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/savedSearches/{idSavedSearch}/pos` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.update_username_by_id`<a id="trellomemberupdate_username_by_id"></a>

updateMembersUsernameByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.update_username_by_id(
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### value: `str`<a id="value-str"></a>

A string with a length of at least 3.  Only lowercase letters, underscores, and numbers are allowed.  Must be unique.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersUsername`](./trello_python_sdk/type/members_username.py)
Attributes of \"Members Username\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/username` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.member.upload_avatar_by_id`<a id="trellomemberupload_avatar_by_id"></a>

addMembersAvatarByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.member.upload_avatar_by_id(
    id_member="idMember_example",
    file="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_member: `str`<a id="id_member-str"></a>

idMember or username

##### file: `str`<a id="file-str"></a>

A file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`MembersAvatar`](./trello_python_sdk/type/members_avatar.py)
Attributes of \"Members Avatar\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/members/{idMember}/avatar` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_board_by_field`<a id="trellonotificationget_board_by_field"></a>

getNotificationsBoardByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_board_by_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/board/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_board_by_id`<a id="trellonotificationget_board_by_id"></a>

getNotificationsBoardByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_board_by_id(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/board` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_by_id`<a id="trellonotificationget_by_id"></a>

getNotificationsByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_by_id(
    id_notification="idNotification_example",
    display="string_example",
    entities="string_example",
    fields="all",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
    board="string_example",
    board_fields="name",
    _list="string_example",
    card="string_example",
    card_fields="name",
    organization="string_example",
    organization_fields="displayName",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### display: `str`<a id="display-str"></a>

 true or false

##### entities: `str`<a id="entities-str"></a>

 true or false

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator, type or unread

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### board: `str`<a id="board-str"></a>

 true or false

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### _list: `str`<a id="_list-str"></a>

 true or false

##### card: `str`<a id="card-str"></a>

 true or false

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### organization: `str`<a id="organization-str"></a>

 true or false

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_by_id_field`<a id="trellonotificationget_by_id_field"></a>

getNotificationsByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_by_id_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_card_by_id`<a id="trellonotificationget_card_by_id"></a>

getNotificationsCardByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_card_by_id(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/card` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_card_by_id_notification_by_field`<a id="trellonotificationget_card_by_id_notification_by_field"></a>

getNotificationsCardByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_card_by_id_notification_by_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/card/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_display_by_id_notification`<a id="trellonotificationget_display_by_id_notification"></a>

getNotificationsDisplayByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_display_by_id_notification(
    id_notification="idNotification_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/display` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_entities_by_id_notification`<a id="trellonotificationget_entities_by_id_notification"></a>

getNotificationsEntitiesByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_entities_by_id_notification(
    id_notification="idNotification_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/entities` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_list_by_id_notification`<a id="trellonotificationget_list_by_id_notification"></a>

getNotificationsListByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_list_by_id_notification(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/list` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_list_by_id_notification_by_field`<a id="trellonotificationget_list_by_id_notification_by_field"></a>

getNotificationsListByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_list_by_id_notification_by_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/list/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_member_by_id_field`<a id="trellonotificationget_member_by_id_field"></a>

getNotificationsMemberByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_member_by_id_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/member/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_member_by_id_notification_by_field`<a id="trellonotificationget_member_by_id_notification_by_field"></a>

getNotificationsMemberCreatorByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_member_by_id_notification_by_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/memberCreator/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_member_by_notification`<a id="trellonotificationget_member_by_notification"></a>

getNotificationsMemberByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_member_by_notification(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/member` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_member_creator_by_id`<a id="trellonotificationget_member_creator_by_id"></a>

getNotificationsMemberCreatorByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_member_creator_by_id(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/memberCreator` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_organization_by_id_notification`<a id="trellonotificationget_organization_by_id_notification"></a>

getNotificationsOrganizationByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_organization_by_id_notification(
    id_notification="idNotification_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/organization` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.get_organization_by_id_notification_by_field`<a id="trellonotificationget_organization_by_id_notification_by_field"></a>

getNotificationsOrganizationByIdNotificationByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.get_organization_by_id_notification_by_field(
    id_notification="idNotification_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/organization/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.mark_all_as_read`<a id="trellonotificationmark_all_as_read"></a>

addNotificationsAllRead()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.mark_all_as_read()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/all/read` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.update_by_id_notification`<a id="trellonotificationupdate_by_id_notification"></a>

updateNotificationsByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.update_by_id_notification(
    id_notification="idNotification_example",
    unread="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### unread: `str`<a id="unread-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Notifications`](./trello_python_sdk/type/notifications.py)
Attributes of \"Notifications\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.notification.update_unread_by_id_notification`<a id="trellonotificationupdate_unread_by_id_notification"></a>

updateNotificationsUnreadByIdNotification()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.notification.update_unread_by_id_notification(
    id_notification="idNotification_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_notification: `str`<a id="id_notification-str"></a>

idNotification

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`NotificationsUnread`](./trello_python_sdk/type/notifications_unread.py)
Attributes of \"Notifications Unread\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/notifications/{idNotification}/unread` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.create`<a id="trelloorganizationcreate"></a>

addOrganizations()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.create(
    desc="string_example",
    display_name="string_example",
    name="string_example",
    prefs_associated_domain="string_example",
    prefs_board_visibility_restrict_org="string_example",
    prefs_board_visibility_restrict_private="string_example",
    prefs_board_visibility_restrict_public="string_example",
    prefs_external_members_disabled="string_example",
    prefs_google_apps_version="string_example",
    prefs_org_invite_restrict="string_example",
    prefs_permission_level="string_example",
    website="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### display_name: `str`<a id="display_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### prefs_associated_domain: `str`<a id="prefs_associated_domain-str"></a>

The google apps domain to link this org to.

##### prefs_board_visibility_restrict_org: `str`<a id="prefs_board_visibility_restrict_org-str"></a>

One of: admin, none or org

##### prefs_board_visibility_restrict_private: `str`<a id="prefs_board_visibility_restrict_private-str"></a>

One of: admin, none or org

##### prefs_board_visibility_restrict_public: `str`<a id="prefs_board_visibility_restrict_public-str"></a>

One of: admin, none or org

##### prefs_external_members_disabled: `str`<a id="prefs_external_members_disabled-str"></a>

 true or false

##### prefs_google_apps_version: `str`<a id="prefs_google_apps_version-str"></a>

a number from 1 to 2

##### prefs_org_invite_restrict: `str`<a id="prefs_org_invite_restrict-str"></a>

An email address with optional expansion tokens

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: private or public

##### website: `str`<a id="website-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Organizations`](./trello_python_sdk/type/organizations.py)
Attributes of \"Organizations\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.delete_prefs_associated_domain_by_id_org`<a id="trelloorganizationdelete_prefs_associated_domain_by_id_org"></a>

deleteOrganizationsPrefsAssociatedDomainByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.delete_prefs_associated_domain_by_id_org(
    id_org="idOrg_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/associatedDomain` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_actions_by_id_org`<a id="trelloorganizationget_actions_by_id_org"></a>

getOrganizationsActionsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_actions_by_id_org(
    id_org="idOrg_example",
    entities="string_example",
    display="string_example",
    filter="all",
    fields="all",
    limit="50",
    format="list",
    since="string_example",
    before="string_example",
    page="0",
    id_models="string_example",
    member="string_example",
    member_fields="avatarHash, fullName, initials and username",
    member_creator="string_example",
    member_creator_fields="avatarHash, fullName, initials and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### entities: `str`<a id="entities-str"></a>

 true or false

##### display: `str`<a id="display-str"></a>

 true or false

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### limit: `str`<a id="limit-str"></a>

a number from 0 to 1000

##### format: `str`<a id="format-str"></a>

One of: count, list or minimal

##### since: `str`<a id="since-str"></a>

A date, null or lastView

##### before: `str`<a id="before-str"></a>

A date, or null

##### page: `str`<a id="page-str"></a>

Page * limit must be less than 1000

##### id_models: `str`<a id="id_models-str"></a>

Only return actions related to these model ids

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_creator: `str`<a id="member_creator-str"></a>

 true or false

##### member_creator_fields: `str`<a id="member_creator_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/actions` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_boards_by_id_org_by_filter`<a id="trelloorganizationget_boards_by_id_org_by_filter"></a>

getOrganizationsBoardsByIdOrgByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_boards_by_id_org_by_filter(
    id_org="idOrg_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/boards/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_boards_by_org_id`<a id="trelloorganizationget_boards_by_org_id"></a>

getOrganizationsBoardsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_boards_by_org_id(
    id_org="idOrg_example",
    filter="all",
    fields="all",
    actions="string_example",
    actions_entities="string_example",
    actions_limit="50",
    actions_format="list",
    actions_since="string_example",
    action_fields="all",
    memberships="none",
    organization="string_example",
    organization_fields="name and displayName",
    lists="none",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### actions_format: `str`<a id="actions_format-str"></a>

One of: count, list or minimal

##### actions_since: `str`<a id="actions_since-str"></a>

A date, null or lastView

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### memberships: `str`<a id="memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### organization: `str`<a id="organization-str"></a>

 true or false

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### lists: `str`<a id="lists-str"></a>

One of: all, closed, none or open

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/boards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_by_id_and_field`<a id="trelloorganizationget_by_id_and_field"></a>

getOrganizationsByIdOrgByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_by_id_and_field(
    id_org="idOrg_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_by_id_org`<a id="trelloorganizationget_by_id_org"></a>

getOrganizationsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_by_id_org(
    id_org="idOrg_example",
    actions="string_example",
    actions_entities="string_example",
    actions_display="string_example",
    actions_limit="50",
    action_fields="all",
    memberships="none",
    memberships_member="string_example",
    memberships_member_fields="fullName and username",
    members="none",
    member_fields="avatarHash, fullName, initials, username and confirmed",
    member_activity="string_example",
    members_invited="none",
    members_invited_fields="avatarHash, initials, fullName and username",
    boards="none",
    board_fields="all",
    board_actions="string_example",
    board_actions_entities="string_example",
    board_actions_display="string_example",
    board_actions_format="list",
    board_actions_since="string_example",
    board_actions_limit="50",
    board_action_fields="all",
    board_lists="none",
    paid_account="string_example",
    fields="name, displayName, desc, descData, url, website, logoHash, products and powerUps",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### actions_entities: `str`<a id="actions_entities-str"></a>

 true or false

##### actions_display: `str`<a id="actions_display-str"></a>

 true or false

##### actions_limit: `str`<a id="actions_limit-str"></a>

a number from 0 to 1000

##### action_fields: `str`<a id="action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### memberships: `str`<a id="memberships-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### memberships_member: `str`<a id="memberships_member-str"></a>

 true or false

##### memberships_member_fields: `str`<a id="memberships_member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members: `str`<a id="members-str"></a>

One of: admins, all, none, normal or owners

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### member_activity: `str`<a id="member_activity-str"></a>

true or false ; works for premium organizations only.

##### members_invited: `str`<a id="members_invited-str"></a>

One of: admins, all, none, normal or owners

##### members_invited_fields: `str`<a id="members_invited_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### boards: `str`<a id="boards-str"></a>

all or a comma-separated list of: closed, members, open, organization, pinned, public, starred or unpinned

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### board_actions: `str`<a id="board_actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### board_actions_entities: `str`<a id="board_actions_entities-str"></a>

 true or false

##### board_actions_display: `str`<a id="board_actions_display-str"></a>

 true or false

##### board_actions_format: `str`<a id="board_actions_format-str"></a>

One of: count, list or minimal

##### board_actions_since: `str`<a id="board_actions_since-str"></a>

A date, null or lastView

##### board_actions_limit: `str`<a id="board_actions_limit-str"></a>

a number from 0 to 1000

##### board_action_fields: `str`<a id="board_action_fields-str"></a>

all or a comma-separated list of: data, date, idMemberCreator or type

##### board_lists: `str`<a id="board_lists-str"></a>

One of: all, closed, none or open

##### paid_account: `str`<a id="paid_account-str"></a>

 true or false

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_members_by_id_org`<a id="trelloorganizationget_members_by_id_org"></a>

getOrganizationsMembersByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_members_by_id_org(
    id_org="idOrg_example",
    filter="all",
    fields="fullName and username",
    activity="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### filter: `str`<a id="filter-str"></a>

One of: admins, all, none, normal or owners

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### activity: `str`<a id="activity-str"></a>

true or false ; works for premium organizations only.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_members_invited_by_id_org`<a id="trelloorganizationget_members_invited_by_id_org"></a>

getOrganizationsMembersInvitedByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_members_invited_by_id_org(
    id_org="idOrg_example",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/membersInvited` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_members_invited_by_id_org_by_field`<a id="trelloorganizationget_members_invited_by_id_org_by_field"></a>

getOrganizationsMembersInvitedByIdOrgByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_members_invited_by_id_org_by_field(
    id_org="idOrg_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/membersInvited/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_memberships_by_id_org_by_id_membership`<a id="trelloorganizationget_memberships_by_id_org_by_id_membership"></a>

getOrganizationsMembershipsByIdOrgByIdMembership()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_memberships_by_id_org_by_id_membership(
    id_org="idOrg_example",
    id_membership="idMembership_example",
    member="string_example",
    member_fields="fullName and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_membership: `str`<a id="id_membership-str"></a>

idMembership

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/memberships/{idMembership}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.get_organization_deltas`<a id="trelloorganizationget_organization_deltas"></a>

getOrganizationsDeltasByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.get_organization_deltas(
    id_org="idOrg_example",
    tags="tags_example",
    ix_last_update="ixLastUpdate_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### tags: `str`<a id="tags-str"></a>

A valid tag for subscribing

##### ix_last_update: `str`<a id="ix_last_update-str"></a>

a number from -1 to Infinity

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/deltas` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.list_members_by_id_org_by_filter`<a id="trelloorganizationlist_members_by_id_org_by_filter"></a>

getOrganizationsMembersByIdOrgByFilter()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.list_members_by_id_org_by_filter(
    id_org="idOrg_example",
    filter="filter_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### filter: `str`<a id="filter-str"></a>

filter

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{filter}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.list_members_cards_by_id_org_by_id_member`<a id="trelloorganizationlist_members_cards_by_id_org_by_id_member"></a>

getOrganizationsMembersCardsByIdOrgByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.list_members_cards_by_id_org_by_id_member(
    id_org="idOrg_example",
    id_member="idMember_example",
    actions="string_example",
    attachments="string_example",
    attachment_fields="all",
    members="string_example",
    member_fields="avatarHash, fullName, initials and username",
    check_item_states="string_example",
    checklists="none",
    board="string_example",
    board_fields="name, desc, closed, idOrganization, pinned, url and prefs",
    _list="string_example",
    list_fields="all",
    filter="visible",
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_member: `str`<a id="id_member-str"></a>

idMember

##### actions: `str`<a id="actions-str"></a>

all or a comma-separated list of: addAttachmentToCard, addChecklistToCard, addMemberToBoard, addMemberToCard, addMemberToOrganization, addToOrganizationBoard, commentCard, convertToCardFromCheckItem, copyBoard, copyCard, copyCommentCard, createBoard, createCard, createList, createOrganization, deleteAttachmentFromCard, deleteBoardInvitation, deleteCard, deleteOrganizationInvitation, disablePowerUp, emailCard, enablePowerUp, makeAdminOfBoard, makeNormalMemberOfBoard, makeNormalMemberOfOrganization, makeObserverOfBoard, memberJoinedTrello, moveCardFromBoard, moveCardToBoard, moveListFromBoard, moveListToBoard, removeChecklistFromCard, removeFromOrganizationBoard, removeMemberFromCard, unconfirmedBoardInvitation, unconfirmedOrganizationInvitation, updateBoard, updateCard, updateCard:closed, updateCard:desc, updateCard:idList, updateCard:name, updateCheckItemStateOnCard, updateChecklist, updateList, updateList:closed, updateList:name, updateMember or updateOrganization

##### attachments: `str`<a id="attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### attachment_fields: `str`<a id="attachment_fields-str"></a>

all or a comma-separated list of: bytes, date, edgeColor, idMember, isUpload, mimeType, name, previews or url

##### members: `str`<a id="members-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### check_item_states: `str`<a id="check_item_states-str"></a>

 true or false

##### checklists: `str`<a id="checklists-str"></a>

One of: all or none

##### board: `str`<a id="board-str"></a>

 true or false

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### _list: `str`<a id="_list-str"></a>

 true or false

##### list_fields: `str`<a id="list_fields-str"></a>

all or a comma-separated list of: closed, idBoard, name, pos or subscribed

##### filter: `str`<a id="filter-str"></a>

One of: all, closed, none, open or visible

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{idMember}/cards` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.list_memberships_by_id_org`<a id="trelloorganizationlist_memberships_by_id_org"></a>

getOrganizationsMembershipsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.list_memberships_by_id_org(
    id_org="idOrg_example",
    filter="all",
    member="string_example",
    member_fields="fullName and username",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### filter: `str`<a id="filter-str"></a>

all or a comma-separated list of: active, admin, deactivated, me or normal

##### member: `str`<a id="member-str"></a>

 true or false

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/memberships` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.remove_by_id_org`<a id="trelloorganizationremove_by_id_org"></a>

deleteOrganizationsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.remove_by_id_org(
    id_org="idOrg_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.remove_invite_restrict_by_id_org`<a id="trelloorganizationremove_invite_restrict_by_id_org"></a>

deleteOrganizationsPrefsOrgInviteRestrictByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.remove_invite_restrict_by_id_org(
    id_org="idOrg_example",
    value="value_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

An email address with optional expansion tokens

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/orgInviteRestrict` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.remove_logo_by_id_org`<a id="trelloorganizationremove_logo_by_id_org"></a>

deleteOrganizationsLogoByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.remove_logo_by_id_org(
    id_org="idOrg_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/logo` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.remove_member_all`<a id="trelloorganizationremove_member_all"></a>

deleteOrganizationsMembersAllByIdOrgByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.remove_member_all(
    id_org="idOrg_example",
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_member: `str`<a id="id_member-str"></a>

idMember

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{idMember}/all` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.remove_member_by_id_org_by_id_member`<a id="trelloorganizationremove_member_by_id_org_by_id_member"></a>

deleteOrganizationsMembersByIdOrgByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.remove_member_by_id_org_by_id_member(
    id_org="idOrg_example",
    id_member="idMember_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_member: `str`<a id="id_member-str"></a>

idMember

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{idMember}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_by_id_org`<a id="trelloorganizationupdate_by_id_org"></a>

updateOrganizationsByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_by_id_org(
    id_org="idOrg_example",
    desc="string_example",
    display_name="string_example",
    name="string_example",
    prefs_associated_domain="string_example",
    prefs_board_visibility_restrict_org="string_example",
    prefs_board_visibility_restrict_private="string_example",
    prefs_board_visibility_restrict_public="string_example",
    prefs_external_members_disabled="string_example",
    prefs_google_apps_version="string_example",
    prefs_org_invite_restrict="string_example",
    prefs_permission_level="string_example",
    website="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### desc: `str`<a id="desc-str"></a>

a string with a length from 0 to 16384

##### display_name: `str`<a id="display_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### name: `str`<a id="name-str"></a>

a string with a length from 0 to 16384

##### prefs_associated_domain: `str`<a id="prefs_associated_domain-str"></a>

The google apps domain to link this org to.

##### prefs_board_visibility_restrict_org: `str`<a id="prefs_board_visibility_restrict_org-str"></a>

One of: admin, none or org

##### prefs_board_visibility_restrict_private: `str`<a id="prefs_board_visibility_restrict_private-str"></a>

One of: admin, none or org

##### prefs_board_visibility_restrict_public: `str`<a id="prefs_board_visibility_restrict_public-str"></a>

One of: admin, none or org

##### prefs_external_members_disabled: `str`<a id="prefs_external_members_disabled-str"></a>

 true or false

##### prefs_google_apps_version: `str`<a id="prefs_google_apps_version-str"></a>

a number from 1 to 2

##### prefs_org_invite_restrict: `str`<a id="prefs_org_invite_restrict-str"></a>

An email address with optional expansion tokens

##### prefs_permission_level: `str`<a id="prefs_permission_level-str"></a>

One of: private or public

##### website: `str`<a id="website-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Organizations`](./trello_python_sdk/type/organizations.py)
Attributes of \"Organizations\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_description_by_id_org`<a id="trelloorganizationupdate_description_by_id_org"></a>

updateOrganizationsDescByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_description_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsDesc`](./trello_python_sdk/type/organizations_desc.py)
Attributes of \"Organizations Desc\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/desc` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_display_name_by_id_org`<a id="trelloorganizationupdate_display_name_by_id_org"></a>

updateOrganizationsDisplayNameByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_display_name_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsDisplayName`](./trello_python_sdk/type/organizations_display_name.py)
Attributes of \"Organizations Display Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/displayName` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_members_by_id_org`<a id="trelloorganizationupdate_members_by_id_org"></a>

updateOrganizationsMembersByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_members_by_id_org(
    id_org="idOrg_example",
    email="string_example",
    full_name="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### email: `str`<a id="email-str"></a>

An email address

##### full_name: `str`<a id="full_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsMembers`](./trello_python_sdk/type/organizations_members.py)
Attributes of \"Organizations Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_members_by_id_org_by_id_member`<a id="trelloorganizationupdate_members_by_id_org_by_id_member"></a>

updateOrganizationsMembersByIdOrgByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_members_by_id_org_by_id_member(
    id_org="idOrg_example",
    id_member="idMember_example",
    email="string_example",
    full_name="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_member: `str`<a id="id_member-str"></a>

idMember

##### email: `str`<a id="email-str"></a>

An email address

##### full_name: `str`<a id="full_name-str"></a>

A string with a length of at least 1.  Cannot begin or end with a space.

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsMembers`](./trello_python_sdk/type/organizations_members.py)
Attributes of \"Organizations Members\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{idMember}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_members_deactivated_by_id_org_by_id_member`<a id="trelloorganizationupdate_members_deactivated_by_id_org_by_id_member"></a>

updateOrganizationsMembersDeactivatedByIdOrgByIdMember()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_members_deactivated_by_id_org_by_id_member(
    id_org="idOrg_example",
    id_member="idMember_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_member: `str`<a id="id_member-str"></a>

idMember

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsMembersDeactivated`](./trello_python_sdk/type/organizations_members_deactivated.py)
Attributes of \"Organizations Members Deactivated\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/members/{idMember}/deactivated` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_membership_by_id_org_by_id_membership`<a id="trelloorganizationupdate_membership_by_id_org_by_id_membership"></a>

updateOrganizationsMembershipsByIdOrgByIdMembership()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_membership_by_id_org_by_id_membership(
    id_org="idOrg_example",
    id_membership="idMembership_example",
    member_fields="string_example",
    type="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### id_membership: `str`<a id="id_membership-str"></a>

idMembership

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### type: `str`<a id="type-str"></a>

One of: admin, normal or observer

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsMemberships`](./trello_python_sdk/type/organizations_memberships.py)
Attributes of \"Organizations Memberships\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/memberships/{idMembership}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_name_by_id_org`<a id="trelloorganizationupdate_name_by_id_org"></a>

updateOrganizationsNameByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_name_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

A string with a length of at least 3.  Only lowercase letters, underscores, and numbers are allowed.  Must be unique.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsName`](./trello_python_sdk/type/organizations_name.py)
Attributes of \"Organizations Name\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/name` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_associated_domain_by_id_org`<a id="trelloorganizationupdate_prefs_associated_domain_by_id_org"></a>

updateOrganizationsPrefsAssociatedDomainByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_associated_domain_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

The google apps domain to link this org to.

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsAssociatedDomain`](./trello_python_sdk/type/prefs_associated_domain.py)
Attributes of \"Prefs Associated Domain\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/associatedDomain` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_board_visibility_restrict_by_id_org`<a id="trelloorganizationupdate_prefs_board_visibility_restrict_by_id_org"></a>

updateOrganizationsPrefsBoardVisibilityRestrictOrgByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_board_visibility_restrict_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

One of: admin, none or org

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsBoardVisibilityRestrict`](./trello_python_sdk/type/prefs_board_visibility_restrict.py)
Attributes of \"Prefs Board Visibility Restrict\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/boardVisibilityRestrict/org` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_board_visibility_restrict_public_by_id_org`<a id="trelloorganizationupdate_prefs_board_visibility_restrict_public_by_id_org"></a>

updateOrganizationsPrefsBoardVisibilityRestrictPublicByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_board_visibility_restrict_public_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

One of: admin, none or org

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsBoardVisibilityRestrict`](./trello_python_sdk/type/prefs_board_visibility_restrict.py)
Attributes of \"Prefs Board Visibility Restrict\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/boardVisibilityRestrict/public` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_external_members_disabled_by_id_org`<a id="trelloorganizationupdate_prefs_external_members_disabled_by_id_org"></a>

updateOrganizationsPrefsExternalMembersDisabledByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_external_members_disabled_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsExternalMembersDisabled`](./trello_python_sdk/type/prefs_external_members_disabled.py)
Attributes of \"Prefs External Members Disabled\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/externalMembersDisabled` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_google_apps_version_by_id_org`<a id="trelloorganizationupdate_prefs_google_apps_version_by_id_org"></a>

updateOrganizationsPrefsGoogleAppsVersionByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_google_apps_version_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

a number from 1 to 2

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsGoogleAppsVersion`](./trello_python_sdk/type/prefs_google_apps_version.py)
Attributes of \"Prefs Google Apps Version\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/googleAppsVersion` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_org_invite_restrict_by_id_org`<a id="trelloorganizationupdate_prefs_org_invite_restrict_by_id_org"></a>

updateOrganizationsPrefsOrgInviteRestrictByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_org_invite_restrict_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

An email address with optional expansion tokens

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsOrgInviteRestrict`](./trello_python_sdk/type/prefs_org_invite_restrict.py)
Attributes of \"Prefs Org Invite Restrict\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/orgInviteRestrict` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_permission_level_by_id_org`<a id="trelloorganizationupdate_prefs_permission_level_by_id_org"></a>

updateOrganizationsPrefsPermissionLevelByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_permission_level_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

One of: private or public

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsPermissionLevel`](./trello_python_sdk/type/prefs_permission_level.py)
Attributes of \"Prefs Permission Level\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/permissionLevel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_prefs_visibility_by_id_org`<a id="trelloorganizationupdate_prefs_visibility_by_id_org"></a>

updateOrganizationsPrefsBoardVisibilityRestrictPrivateByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_prefs_visibility_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

One of: admin, none or org

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PrefsBoardVisibilityRestrict`](./trello_python_sdk/type/prefs_board_visibility_restrict.py)
Attributes of \"Prefs Board Visibility Restrict\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/prefs/boardVisibilityRestrict/private` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.update_website_by_id_org`<a id="trelloorganizationupdate_website_by_id_org"></a>

updateOrganizationsWebsiteByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.update_website_by_id_org(
    id_org="idOrg_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### value: `str`<a id="value-str"></a>

A URL starting with http:// or https:// or null

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsWebsite`](./trello_python_sdk/type/organizations_website.py)
Attributes of \"Organizations Website\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/website` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.organization.upload_logo_by_id_org`<a id="trelloorganizationupload_logo_by_id_org"></a>

addOrganizationsLogoByIdOrg()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.organization.upload_logo_by_id_org(
    id_org="idOrg_example",
    file="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_org: `str`<a id="id_org-str"></a>

idOrg or name

##### file: `str`<a id="file-str"></a>

A file

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`OrganizationsLogo`](./trello_python_sdk/type/organizations_logo.py)
Attributes of \"Organizations Logo\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/organizations/{idOrg}/logo` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.search.find_members`<a id="trellosearchfind_members"></a>

getSearchMembers()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.search.find_members(
    query="query_example",
    limit="8",
    id_board="string_example",
    id_organization="string_example",
    only_org_members="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

a string with a length from 1 to 16384

##### limit: `str`<a id="limit-str"></a>

a number from 1 to 20

##### id_board: `str`<a id="id_board-str"></a>

An id, or null

##### id_organization: `str`<a id="id_organization-str"></a>

An id, or null

##### only_org_members: `str`<a id="only_org_members-str"></a>

A boolean

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search/members` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.search.get_results`<a id="trellosearchget_results"></a>

getSearch()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.search.get_results(
    query="query_example",
    id_organizations="idOrganizations_example",
    id_boards="mine",
    id_cards="string_example",
    model_types="all",
    board_fields="name and idOrganization",
    boards_limit="10",
    card_fields="all",
    cards_limit="10",
    cards_page="0",
    card_board="string_example",
    card_list="string_example",
    card_members="string_example",
    card_stickers="string_example",
    card_attachments="string_example",
    organization_fields="name and displayName",
    organizations_limit="10",
    member_fields="avatarHash, fullName, initials, username and confirmed",
    members_limit="10",
    partial="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### query: `str`<a id="query-str"></a>

a string with a length from 1 to 16384

##### id_organizations: `str`<a id="id_organizations-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### id_boards: `str`<a id="id_boards-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### id_cards: `str`<a id="id_cards-str"></a>

A comma-separated list of objectIds, 24-character hex strings

##### model_types: `str`<a id="model_types-str"></a>

all or a comma-separated list of: actions, boards, cards, members or organizations

##### board_fields: `str`<a id="board_fields-str"></a>

all or a comma-separated list of: closed, dateLastActivity, dateLastView, desc, descData, idOrganization, invitations, invited, labelNames, memberships, name, pinned, powerUps, prefs, shortLink, shortUrl, starred, subscribed or url

##### boards_limit: `str`<a id="boards_limit-str"></a>

a number from 1 to 1000

##### card_fields: `str`<a id="card_fields-str"></a>

all or a comma-separated list of: badges, checkItemStates, closed, dateLastActivity, desc, descData, due, email, idAttachmentCover, idBoard, idChecklists, idLabels, idList, idMembers, idMembersVoted, idShort, labels, manualCoverAttachment, name, pos, shortLink, shortUrl, subscribed or url

##### cards_limit: `str`<a id="cards_limit-str"></a>

a number from 1 to 1000

##### cards_page: `str`<a id="cards_page-str"></a>

a number from 0 to 100

##### card_board: `str`<a id="card_board-str"></a>

 true or false

##### card_list: `str`<a id="card_list-str"></a>

 true or false

##### card_members: `str`<a id="card_members-str"></a>

 true or false

##### card_stickers: `str`<a id="card_stickers-str"></a>

 true or false

##### card_attachments: `str`<a id="card_attachments-str"></a>

A boolean value or &quot;cover&quot; for only card cover attachments

##### organization_fields: `str`<a id="organization_fields-str"></a>

all or a comma-separated list of: billableMemberCount, desc, descData, displayName, idBoards, invitations, invited, logoHash, memberships, name, powerUps, prefs, premiumFeatures, products, url or website

##### organizations_limit: `str`<a id="organizations_limit-str"></a>

a number from 1 to 1000

##### member_fields: `str`<a id="member_fields-str"></a>

all or a comma-separated list of: avatarHash, bio, bioData, confirmed, fullName, idPremOrgsAdmin, initials, memberType, products, status, url or username

##### members_limit: `str`<a id="members_limit-str"></a>

a number from 1 to 1000

##### partial: `str`<a id="partial-str"></a>

 true or false

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/search` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.session.create_and_update`<a id="trellosessioncreate_and_update"></a>

addSessions()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.session.create_and_update(
    id_board="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_board: `str`<a id="id_board-str"></a>

The id of the board you&#39;re viewing.  Boards with no viewers will not get updates about members&#39; statuses.

##### status: `str`<a id="status-str"></a>

One of: active, disconnected or idle

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Sessions`](./trello_python_sdk/type/sessions.py)
Attributes of \"Sessions\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sessions` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.session.get_socket_sessions`<a id="trellosessionget_socket_sessions"></a>

This is the route for WebSocket requests.  See the socket API reference for a description of WebSocket usage.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.session.get_socket_sessions()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sessions/socket` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.session.update_status_by_id_session`<a id="trellosessionupdate_status_by_id_session"></a>

updateSessionsByIdSession()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.session.update_status_by_id_session(
    id_session="idSession_example",
    id_board="string_example",
    status="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_session: `str`<a id="id_session-str"></a>

idSession

##### id_board: `str`<a id="id_board-str"></a>

The id of the board you&#39;re viewing.  Boards with no viewers will not get updates about members&#39; statuses.

##### status: `str`<a id="status-str"></a>

One of: active, disconnected or idle

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Sessions`](./trello_python_sdk/type/sessions.py)
Attributes of \"Sessions\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sessions/{idSession}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.session.update_status_by_id_session_0`<a id="trellosessionupdate_status_by_id_session_0"></a>

updateSessionsStatusByIdSession()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.session.update_status_by_id_session_0(
    id_session="idSession_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_session: `str`<a id="id_session-str"></a>

idSession

##### value: `str`<a id="value-str"></a>

One of: active, disconnected or idle

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`SessionsStatus`](./trello_python_sdk/type/sessions_status.py)
Attributes of \"Sessions Status\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/sessions/{idSession}/status` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.delete_by_token`<a id="trellotokendelete_by_token"></a>

deleteTokensByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.delete_by_token()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_by_token`<a id="trellotokenget_by_token"></a>

getTokensByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_by_token(
    fields="all",
    webhooks="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: dateCreated, dateExpires, idMember, identifier or permissions

##### webhooks: `str`<a id="webhooks-str"></a>

 true or false

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_by_token_by_field`<a id="trellotokenget_by_token_by_field"></a>

getTokensByTokenByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_by_token_by_field(
    token="token_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### token: `str`<a id="token-str"></a>

token

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_member_by_field`<a id="trellotokenget_member_by_field"></a>

getTokensMemberByTokenByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_member_by_field(
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/member/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_member_by_token`<a id="trellotokenget_member_by_token"></a>

getTokensMemberByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_member_by_token(
    fields="all",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### fields: `str`<a id="fields-str"></a>

all or a comma-separated list of: avatarHash, avatarSource, bio, bioData, confirmed, email, fullName, gravatarHash, idBoards, idBoardsPinned, idOrganizations, idPremOrgsAdmin, initials, loginTypes, memberType, oneTimeMessagesDismissed, prefs, premiumFeatures, products, status, status, trophies, uploadedAvatarHash, url or username

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/member` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_webhook_by_id`<a id="trellotokenget_webhook_by_id"></a>

getTokensWebhooksByTokenByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_webhook_by_id(
    id_webhook="idWebhook_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/webhooks/{idWebhook}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.get_webhooks`<a id="trellotokenget_webhooks"></a>

getTokensWebhooksByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.get_webhooks()
```

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/webhooks` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.register_webhook`<a id="trellotokenregister_webhook"></a>

addTokensWebhooksByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.register_webhook(
    description="string_example",
    callback_url="string_example",
    id_model="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

a string with a length from 0 to 16384

##### callback_url: `str`<a id="callback_url-str"></a>

A valid URL that is reachable with a HEAD request

##### id_model: `str`<a id="id_model-str"></a>

id of the model to be monitored

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokensWebhooks`](./trello_python_sdk/type/tokens_webhooks.py)
Attributes of \"Tokens Webhooks\" to be added.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/webhooks` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.remove_by_token_by_id_webhook`<a id="trellotokenremove_by_token_by_id_webhook"></a>

deleteTokensWebhooksByTokenByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.remove_by_token_by_id_webhook(
    id_webhook="idWebhook_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/webhooks/{idWebhook}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.token.update_webhooks_by_token`<a id="trellotokenupdate_webhooks_by_token"></a>

updateTokensWebhooksByToken()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.token.update_webhooks_by_token(
    description="string_example",
    callback_url="string_example",
    id_model="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

a string with a length from 0 to 16384

##### callback_url: `str`<a id="callback_url-str"></a>

A valid URL that is reachable with a HEAD request

##### id_model: `str`<a id="id_model-str"></a>

id of the model to be monitored

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`TokensWebhooks`](./trello_python_sdk/type/tokens_webhooks.py)
Attributes of \"Tokens Webhooks\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/tokens/{token}/webhooks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.type.get_by_id`<a id="trellotypeget_by_id"></a>

getTypesById()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.type.get_by_id(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

id

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/types/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.get_by_id`<a id="trellowebhookget_by_id"></a>

getWebhooksByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.get_by_id(
    id_webhook="idWebhook_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.get_by_id_field`<a id="trellowebhookget_by_id_field"></a>

getWebhooksByIdWebhookByField()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.get_by_id_field(
    id_webhook="idWebhook_example",
    field="field_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### field: `str`<a id="field-str"></a>

field

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}/{field}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.remove_by_id`<a id="trellowebhookremove_by_id"></a>

deleteWebhooksByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.remove_by_id(
    id_webhook="idWebhook_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update`<a id="trellowebhookupdate"></a>

updateWebhooks()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update(
    description="string_example",
    active="string_example",
    callback_url="string_example",
    id_model="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### description: `str`<a id="description-str"></a>

a string with a length from 0 to 16384

##### active: `str`<a id="active-str"></a>

 true or false

##### callback_url: `str`<a id="callback_url-str"></a>

A valid URL that is reachable with a HEAD request

##### id_model: `str`<a id="id_model-str"></a>

id of the model that should be hooked

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Webhooks`](./trello_python_sdk/type/webhooks.py)
Attributes of \"Webhooks\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update_active_by_id`<a id="trellowebhookupdate_active_by_id"></a>

updateWebhooksActiveByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update_active_by_id(
    id_webhook="idWebhook_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### value: `str`<a id="value-str"></a>

 true or false

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksActive`](./trello_python_sdk/type/webhooks_active.py)
Attributes of \"Webhooks Active\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}/active` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update_by_id_webhook`<a id="trellowebhookupdate_by_id_webhook"></a>

updateWebhooksByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update_by_id_webhook(
    id_webhook="idWebhook_example",
    description="string_example",
    active="string_example",
    callback_url="string_example",
    id_model="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### description: `str`<a id="description-str"></a>

a string with a length from 0 to 16384

##### active: `str`<a id="active-str"></a>

 true or false

##### callback_url: `str`<a id="callback_url-str"></a>

A valid URL that is reachable with a HEAD request

##### id_model: `str`<a id="id_model-str"></a>

id of the model that should be hooked

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`Webhooks`](./trello_python_sdk/type/webhooks.py)
Attributes of \"Webhooks\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update_callback_url_by_id`<a id="trellowebhookupdate_callback_url_by_id"></a>

updateWebhooksCallbackURLByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update_callback_url_by_id(
    id_webhook="idWebhook_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### value: `str`<a id="value-str"></a>

A valid URL that is reachable with a HEAD request

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksCallbackURL`](./trello_python_sdk/type/webhooks_callback_url.py)
Attributes of \"Webhooks Callback Url\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}/callbackURL` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update_description_by_id_webhook`<a id="trellowebhookupdate_description_by_id_webhook"></a>

updateWebhooksDescriptionByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update_description_by_id_webhook(
    id_webhook="idWebhook_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### value: `str`<a id="value-str"></a>

a string with a length from 0 to 16384

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksDescription`](./trello_python_sdk/type/webhooks_description.py)
Attributes of \"Webhooks Description\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}/description` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `trello.webhook.update_model_by_id`<a id="trellowebhookupdate_model_by_id"></a>

updateWebhooksIdModelByIdWebhook()

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
trello.webhook.update_model_by_id(
    id_webhook="idWebhook_example",
    value="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id_webhook: `str`<a id="id_webhook-str"></a>

idWebhook

##### value: `str`<a id="value-str"></a>

id of the model to be monitored

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebhooksIdModel`](./trello_python_sdk/type/webhooks_id_model.py)
Attributes of \"Webhooks Id Model\" to be updated.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/webhooks/{idWebhook}/idModel` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)

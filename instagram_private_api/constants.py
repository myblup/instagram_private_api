
class Constants:

    IG_SIG_KEY = 'b45edf687482d21f67e5b2efd36c3fd61222cc138f268f55982a08f2e93a5c95'
    IG_CAPABILITIES = '3ToAAA=='
    SIG_KEY_VERSION = '4'

    APP_VERSION = '10.4.0'
    ANDROID_VERSION = 18
    ANDROID_RELEASE = '4.3'
    PHONE_MANUFACTURER = 'Xiaomi'
    PHONE_DEVICE = 'HM 1SW'
    PHONE_MODEL = 'armani'
    PHONE_DPI = '320dpi'
    PHONE_RESOLUTION = '720x1280'
    PHONE_CHIPSET = 'qcom'

    USER_AGENT_FORMAT = \
        'Instagram %(app_version)s Android (%(android_version)d/%(android_release)s; ' \
        '%(dpi)s; %(resolution)s; %(brand)s; %(device)s; %(model)s; %(chipset)s; en_US)'

    USER_AGENT_EXPRESSION = \
        r'Instagram\s(?P<app_version>[^\s]+)\sAndroid\s\((?P<android_version>[0-9]+)/(?P<android_release>[0-9\.]+);\s' \
        r'(?P<dpi>\d+dpi);\s(?P<resolution>\d+x\d+);\s(?P<manufacturer>[^;]+);\s(?P<device>[^;]+);\s' \
        r'(?P<model>[^;]+);\s(?P<chipset>[^;]+);'

    USER_AGENT = USER_AGENT_FORMAT % {
        'app_version': APP_VERSION,
        'android_version': ANDROID_VERSION,
        'android_release': ANDROID_RELEASE,
        'brand': PHONE_MANUFACTURER,
        'device': PHONE_DEVICE,
        'model': PHONE_MODEL,
        'dpi': PHONE_DPI,
        'resolution': PHONE_RESOLUTION,
        'chipset': PHONE_CHIPSET}

    LOGIN_EXPERIMENTS = 'ig_android_background_phone_confirmation_v2,ig_android_one_click_in_old_flow,ig_android_reg_back_dialog,ig_android_confirmation_code_registration,ig_android_non_fb_sso,ig_android_email_prefill_for_m_in_reg,ig_android_analytics_data_loss,ig_android_prefill_phone_email_login,ig_fbns_blocked,ig_android_contact_point_triage,ig_android_auto_submit_verification_code,ig_android_gmail_oauth_in_reg,ig_fbns_push,ig_android_gmail_oauth_in_access,ig_android_phoneid_sync_interval'   # noqa

    EXPERIMENTS = 'ig_android_ad_holdout_16m5_universe,ig_creation_growth_holdout,ig_android_business_conversion_social_context,ig_android_shopping,ig_android_ad_always_send_ad_attribution_id_universe,ig_android_explore_stories,ig_android_insta_video_abr_resize,ig_android_universe_video_production,ig_android_direct_plus_button,ig_android_ads_heatmap_overlay_universe,ig_android_http_stack_experiment_2016,ig_android_ad_new_sponsored_label_universe,ig_fbns_push,ig_android_follows_you_badge,ig_android_video_playback_bandwidth_threshold,ig_android_direct_link_preview,ig_android_preview_capture,ig_android_stories_book_universe,ig_android_offline_discover_people,android_instagram_prefetch_suggestions_universe,ig_android_histogram_reporter,ig_android_exoplayer_4142,ig_android_disable_comment,ig_android_stories_use_gl_drawing,ig_android_offline_likes_v2,ig_android_high_res_upload_2,ig_android_chaining_teaser_animation,ig_android_2fac,ig_android_react_native_lazy_modules_killswitch,ig_android_offline_snippets_action,ig_android_checkbox_instead_of_button_as_follow_affordance_universe,ig_android_insta_video_audio_encoder,ig_android_image_disk_cache_max_entry_count,ig_android_mark_reel_seen_on_Swipe_forward,ig_android_feed_cold_start,ig_android_mentions_dismiss_rule,ig_android_disable_chroma_subsampling,ig_android_share_spinner,ig_android_video_reuse_surface,ig_explore_v3_android_universe,ig_android_tray_reply_icon,ig_android_offline_follows,ig_android_instavideo_periodic_notif,ig_request_cache_layer,ig_android_stories_teach_gallery_location,ig_android_organic_insights_django,ig_android_follow_request_text_buttons_v3,ig_android_remove_followers_universe,ig_android_boomerang_feed_attribution,ig_fbns_shared,ig_android_offline_others_profile,ig_android_react_native_universe,ig_android_stories_max_video_duration,ig_android_snippets_profile_nux,ig_show_promote_button_in_feed,ig_android_business_conversion_value_prop,ig_android_video_loopcount_int,ig_android_confirmation_code_edit_profile,ig_android_profile_photo_as_media,ig_android_camera_universe,ig_android_offline_follow_list,ig_video_max_duration_qe_preuniverse,ig_android_swipe_navigation_x_angle_universe,ig_android_profile,ig_android_empty_feed_redesign,ig_android_direct_blue_tab,ig_android_video_single_surface,ig_android_enable_share_to_messenger,ig_android_mqtt_skywalker,ig_ranking_following,ig_family_bridges_holdout_universe,ig_android_stories_weblink_creation,ig_android_full_user_detail_endpoint,ig_android_ad_drop_cookie_early,ig_android_pbia_normal_weight_universe,ig_android_feed_preview_blur_fix,ig_android_mute_story,ig_android_inline_gallery_universe,ig_android_view_count_decouple_likes_universe,ig_android_direct_inbox_interactivity,ig_android_etag_layer,ig_android_show_your_story_when_empty_universe_2,ig_android_live_analytics,ig_android_su_activity_feed,ig_android_immersive_viewer,ig_android_family_bridge_discover,ig_android_channels_home,ig_android_dv2_realtime_private_share,ig_android_non_square_first,ig_android_direct_composer,ig_android_video_cache_policy,ig_android_feed_like_social_context,ig_android_react_native_universe_kill_switch,ig_android_follow_search_bar,ig_android_stories_weblink_consumption,ig_android_insta_video_drawing,ig_android_facebook_twitter_profile_photos,ig_android_infinite_scrolling_launch,ig_android_swipeable_filters_blacklist,android_ig_fbns_kill_switch,ig_android_share_to_whatsapp,ig_android_direct_recipients_picker_subtitle_holdout,ig_android_offline_activity_feed,ig_android_capture_hands_free_mode,ig_android_direct_mutually_exclusive_experiment_universe,ig_android_progressive_jpeg,ig_android_swipeablefilters_universe,ig_android_insta_video_sound_always_on,ig_android_share_profile_photo_to_feed_universe,ig_android_direct_drawing_in_quick_cam_universe,ig_android_capture_slowmo_mode,ig_android_render_thumbnail_on_feed,ig_fbns_blocked,ig_fbns_preload_default,ig_android_offline_explore,ig_promotions_unit_in_insights_landing_page,ig_android_post_auto_retry_v7_21,ig_android_direct_typing_indicator,ig_android_ad_zero_latency_logging_universe,ig_android_network_cancellation,ig_android_anrwatchdog,ig_android_search_client_matching,ig_android_user_detail_endpoint,ig_android_os_version_blocking,ig_android_sfplt,ig_android_ad_watchbrowse_universe,ig_android_insta_video_consumption_titles,ig_android_family_bridge_bookmarks,ig_android_offline_main_feed,ig_android_fb_topsearch_sgp_fork_request,ig_android_sidecar,ig_android_explore_story_mute,ig_android_ad_feed_pagination_universe,ig_android_stories_text_enhancements,ig_android_snippets,ig_android_memory_improve_universe,ig_android_media_favorites,ig_android_ad_show_cta_loading_state_universe,ig_android_save_all,ig_android_insta_video_universe,ig_android_stories_device_tilt,ig_android_universe_reel_video_production,ig_android_ontact_invite_universe,ig_android_direct_raven,ig_android_direct_emoji_picker,ig_feed_holdout_universe,ig_android_dynamic_image_disk_cache_size_mb,ig_explore_netego,ig_android_capture_boomerang_mode,ig_android_samsung_app_badging,ig_android_direct_send_auto_retry_universe,ig_android_disk_usage,ig_android_business_page_linked_message,ig_android_business_promotion,ig_android_feed_reshare_button_nux,ig_android_react_native_usertag,ig_android_candy_cane_brsuh_universe,ig_android_insta_video_use_surface_view,ig_fbns_dump_ids,ig_android_feed_header_profile_ring_universe,ig_android_invite_popup_universe,ig_android_direct_raven_reactions,ig_in_feed_commenting,ig_android_new_media_saver,ig_android_rendering_controls,ig_video_copyright_whitelist,ig_android_insta_video_consumption_infra,ig_android_disable_comment_public_test,ig_android_offline_mode_holdout,ig_android_insta_video_consumption,ig_android_fetch_reel_tray_on_resume_universe,ig_android_asset_picker,ig_android_pending_request_search_bar,ig_android_ad_rn_preload_universe,ig_android_fix_ise_two_phase,ig_android_react_native_promote,ig_android_search,ig_android_boomerang_entry,ig_android_newsfeed_large_avatar,ig_android_insta_video_titles_universe,ig_android_send_direct_typing_indicator,ig_android_business_conversion_value_prop_navigate,ig_video_use_sve_universe,ig_android_marauder_update_frequency,ig_offline_profile,ig_android_family_bridge_share,ig_android_exoplayer_holdout,ig_android_add_to_last_post,ig_android_feed_header_profile_ring_open_story_viewer_universe,ig_android_direct_inbox_animation,ig_android_video_captions_universe,ig_android_last_edits,ig_android_video_download_logging,ig_android_ad_carousel_redesign_universe,ig_android_snippets_feed_tooltip,ig_android_ad_new_intent_to_highlight_universe,ig_android_async_network_tweak_universe,ig_android_use_software_layer_for_kc_drawing_universe,ig_android_react_native_ota,ig_android_following_follower_social_context'  # noqa

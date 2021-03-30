from Packages.Main import GoogleAds_main

#define parâmetros
crawler_name = 'google_ads_mkt'
column_names =      ['account', 'active_view_measurable_impr', 'active_view_viewable_impressions', 'headline', 'ad_id', 'ad_group', 'ad_group_id' 
                    ,'all_conversions', 'all_conversions_value', 'app_final_url', 'avg_position', 'call_to_action_responsve_display'
                    ,'call_to_action_text_resp', 'campaign_name', 'campaign_id', 'clicks', 'conversions', 'cost', 'currency'
                    ,'custom_parameter', 'customer_id', 'date', 'description', 'description_1', 'description_2'
                    ,'description_responsve_display', 'destination_url', 'display_url', 'engagements', 'final_url'
                    ,'final_url_suffix', 'gmail_ad_business_name', 'gmail_ad_description', 'gmail_ad_headline', 'gmail_ad_marketing_image_call_to_action_text'
                    ,'gmail_ad_marketing_image_description', 'gmail_ad_marketing_image_headline', 'headline_1', 'headline_2', 'headline_responsve_display'
                    ,'image_ad_url', 'image_ad_name', 'impressions', 'interactions', 'label_id', 'labels', 'long_headline', 'long_headline_responsve_display'
                    ,'mobile_final_url', 'network', 'path_1', 'path_2', 'price_fix_responsve_display'
                    ,'price_prefix_resp', 'promotion_text_resp'
                    ]

#name = ['CAMPAIGN_PERFORMANCE_REPORT','ADGROUP_PERFORMANCE_REPORT','AD_PERFORMANCE_REPORT','SEARCH_QUERY_PERFORMANCE_REPORT','KEYWORDS_PERFORMANCE_REPORT']
name = ['AD_PERFORMANCE_REPORT','CAMPAIGN_PERFORMANCE_REPORT']
date_range_type = 'CUSTOM_DATE'
#report_type = ['CAMPAIGN_PERFORMANCE_REPORT','ADGROUP_PERFORMANCE_REPORT','AD_PERFORMANCE_REPORT','SEARCH_QUERY_PERFORMANCE_REPORT','KEYWORDS_PERFORMANCE_REPORT']
report_type = ['AD_PERFORMANCE_REPORT','CAMPAIGN_PERFORMANCE_REPORT']
download_format = 'CSV'
query_date_range = {'min':'20201201','max':'20201231'} 

query_fields = [['AccountDescriptiveName', 'ActiveViewMeasurability', 'ActiveViewImpressions', 'Headline', 'Id', 'AdGroupName', 'AdGroupId'
                    ,'AllConversions', 'AllConversionValue', 'CreativeFinalAppUrls', 'AveragePosition', 'MultiAssetResponsiveDisplayAdCallToActionText'
                    ,'CallToActionText', 'CampaignName', 'CampaignId', 'Clicks', 'Conversions', 'Cost', 'AccountCurrencyCode'
                    ,'CreativeUrlCustomParameters', 'ExternalCustomerId', 'Date', 'Description', 'Description1', 'Description2'
                    ,'MultiAssetResponsiveDisplayAdDescriptions', 'CreativeDestinationUrl', 'DisplayUrl', 'Engagements', 'CreativeFinalUrls'
                    ,'CreativeFinalUrlSuffix', 'GmailTeaserBusinessName', 'GmailTeaserDescription', 'GmailTeaserHeadline', 'MarketingImageCallToActionText'
                    ,'MarketingImageDescription', 'MarketingImageHeadline', 'HeadlinePart1', 'HeadlinePart2', 'MultiAssetResponsiveDisplayAdHeadlines'
                    ,'ImageAdUrl', 'ImageCreativeName', 'Impressions', 'Interactions', 'LabelIds', 'Labels', 'LongHeadline', 'MultiAssetResponsiveDisplayAdLongHeadline'
                    ,'CreativeFinalMobileUrls', 'AdNetworkType1', 'Path1', 'Path2', 'MultiAssetResponsiveDisplayAdDynamicSettingsPricePrefix'
                    ,'PricePrefix', 'MultiAssetResponsiveDisplayAdDynamicSettingsPromoText'
                ],
                ['AccountDescriptiveName','AdNetworkType1','AdvertisingChannelSubType','AdvertisingChannelType','AllConversions','Amount'
                ,'AveragePosition','BiddingStrategyType','CampaignId','CampaignName','CampaignStatus','Clicks','Conversions','Cost'
                ,'Date','ExternalCustomerId','FinalUrlSuffix','Impressions','SearchBudgetLostImpressionShare','SearchImpressionShare'
                ,'SearchRankLostImpressionShare','TrackingUrlTemplate','UrlCustomParameters','VideoQuartile100Rate','VideoQuartile75Rate'
                ,'VideoQuartile50Rate','VideoQuartile25Rate','VideoViews']
                
                ]

#executa main
GoogleAds_main.main(crawler_name,column_names,name, date_range_type, report_type, download_format, query_fields, query_date_range)
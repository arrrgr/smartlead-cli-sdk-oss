# Smartlead SDK Agent - Skills Reference

This is the complete list of what the Smartlead AI agent can do. There are **170 tools across 13 modules**, covering roughly 91% of Smartlead's API surface.

You don't need to memorize tool names or parameters. Just ask in plain English and the agent figures out which tool to call, what parameters to pass, and how to format the results.

---

## 1. Campaigns

| Skill | What it does | Example prompt |
|---|---|---|
| Create campaign | Create a new empty campaign | "Create a new campaign called Q2 SaaS Founders" |
| Get campaign | Fetch details for a specific campaign by ID | "Show me campaign 3021197" |
| Delete campaign | Permanently delete a campaign | "Delete campaign 3048201" |
| Update schedule | Change sending schedule (days, times, timezone) | "Set campaign 3021197 to send Mon-Fri 9am-5pm EST" |
| Update settings | Change campaign settings (tracking, daily limit, etc.) | "Turn off open tracking on campaign 3021197" |
| Update status | Start, pause, or complete a campaign | "Pause campaign 3021197" |
| List campaigns by lead | Find all campaigns a specific lead is in | "What campaigns is lead 88421 part of?" |
| Export campaign data | Export all lead data from a campaign as CSV | "Export the leads from campaign 3021197" |
| Create subsequence | Create a subsequence (follow-up branch) for a campaign | "Create a subsequence for campaign 3021197 called 'Interested Path'" |

---

## 2. Leads

| Skill | What it does | Example prompt |
|---|---|---|
| Add leads to campaign | Upload one or more leads into a campaign | "Add these 50 leads to campaign 3021197" |
| List campaign leads | Get leads in a campaign with optional filters | "Show me all leads in campaign 3021197 with status 'replied'" |
| Get lead by email | Look up a lead across all campaigns by email address | "Find the lead with email john@acme.com" |
| List global leads | Browse all leads across your account | "Show me all leads added in the last 7 days" |
| List lead categories | Get all available lead categories (Interested, Not Interested, etc.) | "What lead categories do I have?" |
| Update lead | Change a lead's email, name, or custom fields | "Update lead 44219 in campaign 3021197 with new email john.doe@acme.com" |
| Update lead category | Categorize a lead (e.g., mark as Interested) | "Mark lead 44219 in campaign 3021197 as Interested" |
| Resume lead | Unpause a lead so sequences continue | "Resume lead 44219 in campaign 3021197" |
| Pause lead | Pause sending to a specific lead | "Pause lead 44219 in campaign 3021197" |
| Delete lead | Remove a lead from a campaign | "Remove lead 44219 from campaign 3021197" |
| Unsubscribe lead | Unsubscribe a lead from a specific campaign | "Unsubscribe lead 44219 from campaign 3021197" |
| Unsubscribe globally | Unsubscribe a lead from all campaigns | "Globally unsubscribe lead 44219 from everything" |
| Get campaign overview | See a lead's status across all campaigns they are in | "Show me all campaigns lead 44219 is enrolled in and their status" |
| Get sequence details | See which sequence step a lead is at | "What step is lead 44219 on?" |
| Get message history | See all emails sent/received for a lead in a campaign | "Show me the full email thread with lead 44219 in campaign 3021197" |
| Move leads to list | Move leads to an inactive/do-not-contact list | "Move bounced leads from campaign 3021197 to list 5521" |
| Push leads to campaign | Push existing leads into a different campaign | "Move leads 44219 and 44220 into campaign 3021198" |

---

## 3. Email Accounts

| Skill | What it does | Example prompt |
|---|---|---|
| Create email account | Add a new SMTP/IMAP email account | "Add a new mailbox sender@growthgrid.co with these SMTP settings" |
| List all accounts | Get all email accounts in your workspace | "Show me all my email accounts" |
| Get email account | Fetch details for a specific email account | "Show me email account 12045" |
| Update email account | Change SMTP/IMAP settings, daily limit, or signature | "Update the daily send limit on account 12045 to 30" |
| Add accounts to campaign | Attach email accounts to a campaign for sending | "Add mailboxes 12045 and 12046 to campaign 3021197" |
| Remove accounts from campaign | Detach email accounts from a campaign | "Remove mailbox 12045 from campaign 3021197" |
| List campaign accounts | See which email accounts are assigned to a campaign | "What mailboxes are sending for campaign 3021197?" |
| Update warmup settings | Change warmup config (daily ramp, reply rate, etc.) | "Set warmup on account 12045 to 3 emails per day with 40% reply rate" |
| Get warmup stats | Check warmup progress and deliverability | "How is the warmup going on account 12045?" |
| Reconnect failed accounts | Attempt to reconnect all failed/disconnected accounts | "Reconnect all my failed email accounts" |
| Fetch messages | Pull sent/received messages for an account in a date range | "Show me emails sent from account 12045 last week" |
| Delete email account | Remove an email account | "Delete email account 12045" |
| Bulk delete accounts | Delete multiple email accounts at once | "Delete email accounts 12045, 12046, and 12047" |
| Save OAuth account | Add a Google/Microsoft OAuth email account | "Connect my Google Workspace account via OAuth" |
| Disconnect Google | Disconnect a Google OAuth account | "Disconnect Google from email account 12045" |
| Disconnect Microsoft | Disconnect a Microsoft OAuth account | "Disconnect Microsoft from email account 12045" |

---

## 4. Sequences

| Skill | What it does | Example prompt |
|---|---|---|
| Get sequences | Fetch all email steps in a campaign's sequence | "Show me the sequences for campaign 3021197" |
| Save sequences | Create or update the email steps for a campaign | "Set up a 3-step sequence for campaign 3021197 with these subject lines and bodies" |

---

## 5. Analytics (Campaign-Level)

| Skill | What it does | Example prompt |
|---|---|---|
| Get campaign statistics | Full stats: sent, opened, replied, bounced, etc. | "What are the stats for campaign 3021197?" |
| Get top-level analytics | High-level campaign performance overview | "Give me a quick overview of campaign 3021197 performance" |
| Get analytics by date range | Stats filtered to a specific date window | "Show me campaign 3021197 stats from March 1 to March 15" |
| Get top-level analytics by date | High-level stats for a date range | "How did campaign 3021197 perform last week?" |
| Get lead statistics | Lead-level breakdown (how many in each status) | "How many leads in campaign 3021197 are in each status?" |
| Get mailbox statistics | Per-mailbox sending stats for a campaign | "Which mailboxes are performing best in campaign 3021197?" |
| Get sequence analytics | Performance breakdown by sequence step | "Which email step gets the most replies in campaign 3021197?" |
| Get variant statistics | A/B test variant performance comparison | "Compare variant A vs variant B in campaign 3021197" |
| Get warmup stats | Email account warmup statistics | "What are the warmup stats for email account 12045?" |

---

## 6. Global Analytics

| Skill | What it does | Example prompt |
|---|---|---|
| Campaign list | List all campaigns with summary stats | "Show me all my campaigns and their stats" |
| Client list | List all clients with summary stats | "Show me all my agency clients and their numbers" |
| Client monthly count | Client activity broken down by month | "How many emails did each client send per month?" |
| Overall stats (v2) | Account-wide totals: sent, opened, replied, bounced | "What are my overall sending stats across all campaigns?" |
| Daily stats | Day-by-day performance breakdown | "Show me daily send/open/reply stats for the last 30 days" |
| Daily stats by sent time | Daily stats grouped by when emails were sent | "Break down my stats by send time for this month" |
| Daily positive replies | Positive reply count by day | "How many positive replies did I get each day this week?" |
| Daily positive replies by sent time | Positive replies grouped by send time | "Show positive replies by send date for March" |
| Campaign overall stats | Aggregate stats for one or all campaigns | "Give me total stats across all campaigns" |
| Client overall stats | Aggregate stats for a specific client | "What are client 191128's total stats?" |
| Mailbox health by name | Deliverability health per mailbox | "Which mailboxes have the worst deliverability?" |
| Mailbox health by domain | Deliverability health per sending domain | "How is growthgridgo.co performing across all mailboxes?" |
| Mailbox performance by provider | Stats broken down by email provider (Gmail, Outlook, etc.) | "How are my emails performing on Gmail vs Outlook?" |
| Team stats | Team member performance overview | "Show me how each team member is performing" |
| Lead overall stats | Global lead status breakdown | "How many total leads do I have and what status are they in?" |
| Lead category responses | Response stats grouped by lead category | "How many replies came from leads marked Interested?" |
| First reply stats | How many leads were contacted before first reply | "How many emails does it take before a lead replies?" |
| Follow-up reply rate | Reply rates on follow-up steps vs initial email | "What is the reply rate on my follow-ups vs first emails?" |
| Lead reply time | Time between sending and lead replying | "How long does it take leads to reply on average?" |
| Campaign response stats | Response breakdown across campaigns | "Which campaigns have the highest response rates?" |
| Campaign status stats | Campaign counts by status (active, paused, completed) | "How many campaigns are active vs paused?" |
| Mailbox overall stats | Global mailbox performance summary | "Give me overall stats for all my mailboxes" |

---

## 7. Webhooks

| Skill | What it does | Example prompt |
|---|---|---|
| List webhooks | Get all webhooks configured for a campaign | "What webhooks are set up on campaign 3021197?" |
| Create/update webhook | Add or update a webhook URL and event triggers | "Set up a webhook on campaign 3021197 to hit https://hooks.example.com/reply on replies" |
| Delete webhook | Remove a webhook from a campaign | "Delete the webhook on campaign 3021197" |
| Get webhook summary | See webhook delivery stats (success, failed, pending) | "How are the webhooks performing on campaign 3021197?" |
| Retrigger failed webhooks | Retry all failed webhook deliveries for a campaign | "Retrigger the failed webhooks on campaign 3021197" |

---

## 8. Block List

| Skill | What it does | Example prompt |
|---|---|---|
| Add to block list | Block domains or emails from receiving outreach | "Block the domains competitor.com and noreply.com" |
| List block list | View all blocked domains and emails | "Show me my full block list" |
| Delete from block list | Remove an entry from the block list | "Unblock competitor.com from the block list" |

---

## 9. Clients

| Skill | What it does | Example prompt |
|---|---|---|
| Create client | Add a new agency client | "Create a new client called Acme Corp" |
| List all clients | Get all clients in your agency account | "Show me all my clients" |
| Create API key | Generate an API key for a client | "Create an API key for client 191128" |
| List API keys | View all client API keys | "Show me all API keys" |
| Delete API key | Remove a client API key | "Delete API key 4421" |
| Reset API key | Rotate/regenerate a client API key | "Reset the API key 4421" |

---

## 10. Unified Inbox (Master Inbox)

| Skill | What it does | Example prompt |
|---|---|---|
| Get replies | Fetch inbox replies with filters and sorting | "Show me all unread replies from this week" |
| Get lead details | Get full details for a specific inbox lead | "Show me inbox lead 88421" |
| Reply to lead | Send a reply in an email thread | "Reply to lead 88421 in campaign 3021197 saying we'd love to set up a call" |
| Forward email | Forward a lead's email thread to someone | "Forward the thread with lead 88421 to my sales manager" |
| Update revenue | Set the deal revenue value on a lead | "Set revenue on inbox lead 88421 to $15,000" |
| Update category | Change a lead's category from the inbox | "Mark inbox lead 88421 as Interested" |
| Get snoozed | View snoozed inbox messages | "Show me all snoozed messages" |
| Get important | View messages marked as important | "Show me important messages" |
| Get scheduled | View scheduled outgoing messages | "What emails are scheduled to go out?" |
| Get reminders | View inbox reminders | "Show me my follow-up reminders" |
| Get archived | View archived inbox messages | "Show me archived messages" |
| Get untracked | View replies that could not be matched to a campaign | "Show me any untracked replies" |
| Update read status | Mark a message as read or unread | "Mark inbox lead 88421 as read" |
| Set reminder | Create a reminder to follow up with a lead | "Remind me to follow up with inbox lead 88421 in 3 days" |
| Create task | Create a task linked to a lead | "Create a task for lead 88421: send proposal by Friday" |
| Create note | Add a note to a lead | "Add a note to lead 88421: spoke with them on the phone, very interested" |
| Push to subsequence | Move a lead into a subsequence | "Push inbox lead 88421 into subsequence 3021199" |
| Assign team member | Assign a lead to a team member | "Assign lead 88421 to team member 5" |
| Block domains | Block domains directly from the inbox | "Block the domain spammer.com from the inbox" |
| Resume lead | Resume a paused lead from the inbox | "Resume inbox lead 88421" |

---

## 11. Smart Delivery

| Skill | What it does | Example prompt |
|---|---|---|
| Get providers | List available testing providers and regions | "What inbox providers can I test against?" |
| Create manual test | Run a one-time deliverability test | "Run a spam test on my growthgridgo.co mailboxes" |
| Create automated test | Set up recurring deliverability tests | "Set up automated weekly spam testing for campaign 3021197" |
| Get test | Fetch results for a specific test | "Show me the results of spam test 7821" |
| Delete tests | Remove deliverability test records | "Delete spam tests 7821 and 7822" |
| Stop automated test | Cancel a recurring automated test | "Stop the automated spam test 7821" |
| List tests | Browse all deliverability tests | "Show me all my spam tests" |
| Get provider report | Inbox placement by provider (Gmail, Outlook, Yahoo) | "Where did my test emails land on Gmail vs Outlook?" |
| Get geo report | Inbox placement by geographic region | "How is deliverability in the US vs Europe?" |
| Get sender report | Per-sender account deliverability results | "Which sender accounts have the best inbox placement?" |
| Get spam filter report | Spam filter detection details | "Did any spam filters flag my test emails?" |
| Get DKIM details | DKIM authentication results | "Check DKIM for spam test 7821" |
| Get SPF details | SPF authentication results | "Check SPF records for spam test 7821" |
| Get rDNS | Reverse DNS lookup results | "Check reverse DNS for spam test 7821" |
| Get sender accounts | List sender accounts used in a test | "What mailboxes were used in spam test 7821?" |
| Get IP blacklists | Check if sending IPs are blacklisted | "Are any of my IPs blacklisted in test 7821?" |
| Get domain blacklist | Check if sending domains are blacklisted | "Is my domain blacklisted?" |
| Get test email content | View the actual email content sent during a test | "Show me what email was sent in spam test 7821" |
| Get IP blacklist count | Count of blacklist hits for sending IPs | "How many blacklists am I on in test 7821?" |
| Get email headers | View raw email headers from a test | "Show me the email headers from spam test 7821" |
| Get schedule history | View run history for an automated test | "When did automated test 7821 last run?" |
| Get IP details | IP address information for a test | "What IP addresses were used in test 7821?" |
| Get mailbox summary | Inbox/spam/missing breakdown per mailbox | "Give me the mailbox placement summary for test 7821" |
| Get mailbox count | Count of mailboxes tested | "How many mailboxes were included in test 7821?" |
| List folders | Get all test organization folders | "Show me my spam test folders" |
| Create folder | Create a new folder to organize tests | "Create a folder called Q2 Deliverability Tests" |
| Get folder | Get details of a specific folder | "Show me folder 14" |
| Delete folder | Remove a test folder | "Delete folder 14" |

---

## 12. Smart Prospect

| Skill | What it does | Example prompt |
|---|---|---|
| Get departments | List available department filters | "What departments can I filter by?" |
| Get cities | Search for city filters | "Search for cities matching 'San Francisco'" |
| Get countries | List available country filters | "What countries can I filter prospects by?" |
| Get states | List states for a country | "Show me all US states I can filter by" |
| Get industries | List available industry filters | "What industries are available for prospecting?" |
| Get sub-industries | List sub-industries within an industry | "What sub-industries are under SaaS?" |
| Get head counts | List company size (employee count) filters | "What company size ranges can I filter by?" |
| Get levels | List seniority level filters | "What seniority levels can I search for?" |
| Get revenue options | List company revenue range filters | "What revenue ranges can I filter companies by?" |
| Get companies | Search for companies by name | "Search for companies matching 'Salesforce'" |
| Get domains | Search for company domains | "Search for domains matching 'acme'" |
| Get job titles | Search for job title filters | "Search for job titles matching 'VP Sales'" |
| Get keywords | Search for keyword filters | "Search for keywords matching 'cold email'" |
| Search contacts | Search the prospect database with filters | "Find VPs of Sales at SaaS companies with 50-200 employees in the US" |
| Fetch contacts | Retrieve full contact details (consumes credits) | "Fetch the full details for contacts 1001, 1002, and 1003" |
| Get contacts | Get previously fetched contact details | "Show me contacts 1001, 1002, and 1003" |
| Review contacts | Approve or reject fetched contacts | "Approve contacts 1001 and 1002, reject 1003" |
| Get saved searches | List all saved prospect searches | "Show me my saved searches" |
| Get recent searches | List recent prospect searches | "What searches have I run recently?" |
| Get fetched searches | List searches where contacts were fetched | "Show me searches where I actually pulled contacts" |
| Save search | Save a prospect search for later use | "Save this search as 'SaaS VP Sales US'" |
| Update saved search | Modify filters on a saved search | "Update my saved search to include companies with 200-500 employees" |
| Update fetched lead | Edit data on a fetched prospect | "Update the phone number on prospect 1001" |
| Get search analytics | View prospecting search usage stats | "How many prospect searches have I run this month?" |
| Get reply analytics | View reply rates for prospects found via Smart Prospect | "What is the reply rate on leads I found through Smart Prospect?" |
| Find emails | Find email addresses for a contact | "Find the email for John Smith at acme.com" |

---

## 13. Smart Senders

| Skill | What it does | Example prompt |
|---|---|---|
| Get mailbox OTP | Get one-time password for mailbox setup | "Get the OTP for mailbox setup" |
| Auto-generate mailboxes | Generate mailbox configurations automatically | "Auto-generate mailboxes for my new domains" |
| Search domain | Check domain availability for purchase | "Is the domain coldoutreach.co available?" |
| Get vendors | List available domain vendors | "What domain vendors are available?" |
| Place order | Purchase a domain through Smartlead | "Buy the domain coldoutreach.co" |
| List domains | View all purchased/managed domains | "Show me all my sending domains" |
| Get order details | Check status of a domain order | "What is the status of my domain order 3344?" |

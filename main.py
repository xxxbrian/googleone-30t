from playwright.sync_api import sync_playwright
import time
captured_url = None

def check_response(response):
    global captured_url
    if response.url.startswith('https://tokenized.play.google.com/eacquire/subscription'):
        captured_url = response.url
    return response.url.startswith('https://tokenized.play.google.com/eacquire/subscription')

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.on("request", capturer.handle_request)
    page.goto("https://accounts.google.com/signin")
    
    input("Please manually log in to your Google account, and then press Enter to continue...")

    cookies = page.context.cookies()
    # print("Cookies:", cookies)

    page.goto("https://payments.google.com/")
    input("Please manually add payments to your Google account, and then press Enter to continue...")
    
    ###################################################################
    # Magic Link
    page.goto("https://tokenized.play.google.com/eacquire/subscription?authuser=0&ear=%5B%5B%22subs%3Acom.google.android.apps.subscriptions.red%3Ag1.2tb.6months_eft%22%2C21%5D%2Cnull%2C%5Bnull%2Cnull%2C%22%2Fu%2F0%2Finapp%2Fpurchase%3Forigin%3Dhttps%253A%252F%252Fphotos.google.com%26utm_medium%3Dweb%26utm_source%3Dphotos%26utm_campaign%3Dphotos_storage_near_quota%26usegapi%3D1%26jsh%3Dm%253B%252F_%252Fscs%252Fabc-static%252F_%252Fjs%252Fk%253Dgapi.gapi.en.Ox0HebTIzao.O%252Fd%253D1%252Frs%253DAHpOoo9JBE0z9__nE4FgyS-eLRbRwEP9Gw%252Fm%253D__features__%22%2C%5B%22https%3A%2F%2Fphotos.google.com%22%5D%5D%2Cnull%2C%5B%22W1tudWxsLG51bGwsbnVsbCxbbnVsbCxbIlJzMi4wLjY6OjpzMTEsMiwyNmI1ZTE5LDAsNzgwLGEwNjNlYmU5LDAsNDM4LGVkZDk4YmFjLDAsMTgsNDg2M2ZkMzUsMCw3ODAsY2IyZDVjNmYsMCw0MDgsNmFkNDdjNmMsMCw0MTksN2JkYjQ5ZjYsMCwzOWIsYjY1NDAyMDAsMCw3ODAsZWVhODIwYjYsMCw0MDgsMWFhNDMzMSwwLFwiV2luMzIsZjU0NjgzZjIsMCxcIkdvb2dsZSBJbmMuLGFmNzk0NTE1LDAsXCI1LjAgMjhXaW5kb3dzIE5UIDEwLjAzYiBXaW42NDNiIHg2NDI5IEFwcGxlV2ViS2l0MmY1MzcuMzYgMjhLSFRNTDJjIGxpa2UgR2Vja28yOSBDaHJvbWUyZjExNi4wLjAuMCBTYWZhcmkyZjUzNy4zNixkODE3MjNkMSwwLFwidmksNWNjM2FiNWYsMCxcIk1vemlsbGEyZjUuMCAyOFdpbmRvd3MgTlQgMTAuMDNiIFdpbjY0M2IgeDY0MjkgQXBwbGVXZWJLaXQyZjUzNy4zNiAyOEtIVE1MMmMgbGlrZSBHZWNrbzI5IENocm9tZTJmMTE2LjAuMC4wIFNhZmFyaTJmNTM3LjM2LDI0YTY2ZGY2LDAsLTFhNCxcIlRodSBKYW4gMDEgMTk3MCAwNzNhMDAzYTAwIEdNVDJiMDcwMCAyOEluZG9jaGluYSBUaW1lMjksMmNhMDU1NGYsXCJQREYgVmlld2VyLDAsXCJQb3J0YWJsZSBEb2N1bWVudCBGb3JtYXQsXCJDaHJvbWUgUERGIFZpZXdlciwwLFwiUG9ydGFibGUgRG9jdW1lbnQgRm9ybWF0LFwiQ2hyb21pdW0gUERGIFZpZXdlciwwLFwiUG9ydGFibGUgRG9jdW1lbnQgRm9ybWF0LFwiTWljcm9zb2Z0IEVkZ2UgUERGIFZpZXdlciwwLFwiUG9ydGFibGUgRG9jdW1lbnQgRm9ybWF0LFwiV2ViS2l0IGJ1aWx0MmRpbiBQREYsMCxcIlBvcnRhYmxlIERvY3VtZW50IEZvcm1hdCw2YzhiOWQ1Yiw3NzBjNjdmYywwLDA6YTIxLDMsMThhY2EzZjFhMDMsMCw4NCwxOmE0MCxcImYsMThhY2EzZjFhMDQiXSwiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiaHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tIixudWxsLFtdLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdXSxudWxsLG51bGwsInZpIiwxLDEsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLFtdLFtdLG51bGwsbnVsbCxbXSxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsbnVsbCxudWxsLG51bGwsW11dLFsiaHR0cHM6Ly9wYXltZW50cy5nb29nbGUuY29tL3BheW1lbnRzL3JlZGlyZWN0X2Zvcm1fbGFuZGluZz9zdWNjZXNzPXRydWUiLCJodHRwczovL3BheW1lbnRzLmdvb2dsZS5jb20vcGF5bWVudHMvcmVkaXJlY3RfZm9ybV9sYW5kaW5nP3N1Y2Nlc3M9ZmFsc2UiLG51bGwsW11dLFtdXQ%3D%3D%22%5D%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22ChcIAxBCGAE6Dy9pbmFwcC9wdXJjaGFzZQ%3D%3D%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C1%5D&parent=https%3A%2F%2Fphotos.google.com&usegapi=1&id=I0_1695610247742&_gfid=I0_1695610247742&parent=https%3A%2F%2Fone.google.com&pfname=%2FI0_1695610132341&rpctoken=15168347&jsh=m%3B%2F_%2Fscs%2Fabc-static%2F_%2Fjs%2Fk%3Dgapi.gapi.en.Ox0HebTIzao.O%2Fd%3D1%2Frs%3DAHpOoo9JBE0z9__nE4FgyS-eLRbRwEP9Gw%2Fm%3D__features__&utm_source=j2team&utm_medium=url_shortener&utm_campaign=Token")

    # Trial Subscribe
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    # page.wait_for_load_state("networkidle")
    time.sleep(5)

    ###################################################################
    # Change Plan to 30T
    page.goto("https://one.google.com/plans")
    page.get_by_role("button", name="More options").click()
    with page.expect_event("response", predicate=check_response) as response_info:
        page.click('[data-sku-id="g1.30tb"]')
    
    # 30T Subscribe
    next_page = str(captured_url).replace('2C5','2C3')
    page.goto(next_page)
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    time.sleep(5)

    ###################################################################
    # Change Plan to 2T
    page.goto("https://one.google.com/u/0/settings")
    page.get_by_role("button", name="Change membership plan").click()
    with page.expect_event("response", predicate=check_response) as response_info:
        page.click('[data-sku-id="g1.2tb.annual"]')

    # 2T Subscribe
    next_page = str(captured_url).replace('2C6','2C1')
    page.goto(next_page)
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    time.sleep(5)

    ###################################################################
    # Change Plan to 30T
    page.goto("https://one.google.com/u/0/settings")
    page.get_by_role("button", name="Change membership plan").click()
    with page.expect_event("response", predicate=check_response) as response_info:
        page.click('[data-sku-id="g1.20tb"]')
    
    # 30T Subscribe
    next_page = str(captured_url).replace('2C5','2C3')
    page.goto(next_page)
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    time.sleep(5)

    ###################################################################
    # Change Plan to 5T
    page.goto("https://one.google.com/u/0/settings")
    page.get_by_role("button", name="Change membership plan").click()
    with page.expect_event("response", predicate=check_response) as response_info:
        page.click('[data-sku-id="g1.5tb.annual"]')
    
    # 5T Subscribe
    next_page = str(captured_url).replace('2C6','2C1')
    page.goto(next_page)
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    time.sleep(5)

    ###################################################################
    # Change Plan to 30T
    page.goto("https://one.google.com/u/0/settings")
    page.get_by_role("button", name="Change membership plan").click()
    with page.expect_event("response", predicate=check_response) as response_info:
        page.click('[data-sku-id="g1.20tb"]')
    
    # 30T Subscribe
    next_page = str(captured_url).replace('2C5','2C3')
    page.goto(next_page)
    page.wait_for_selector("#buy-button", state="attached")
    page.click(":nth-match(#buy-button, 2)")
    # page.get_by_role("button", name="Subscribe").click()
    time.sleep(5)

    ###################################################################
    # FINISH
    page.goto("https://one.google.com")
    input("Finished, press Enter to exit...")
    browser.close()
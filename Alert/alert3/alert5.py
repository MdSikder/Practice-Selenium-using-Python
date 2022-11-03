

def frame_switch(css_selector):
  driver.switch_to.frame(driver.find_element_by_css_selector(css_selector))
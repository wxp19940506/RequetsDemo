#-*- coding:utf-8 -*-
from lxml import etree

text = '''
    <table id="hhotzw">
	    				    				<tbody><tr>
	    					<td>
	    						<a href="position_detail.php?id=45917" title="CDG064-web前端开发工程师（上海）">CDG064-web前端开发工程...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2175">上海</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45887" title="21882-算法工程师（深圳）">21882-算法工程师（深圳）</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45868" title="CSIG02-腾讯云行业交付架构师（深圳）">CSIG02-腾讯云行业交付...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45870" title="ZSC-Senior Patent Counsel/Expert">ZSC-Senior Patent C...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45851" title="15616-高级手游系统策划（上海）">15616-高级手游系统策划（...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2175">上海</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45842" title="15570-新项目资深主美（深圳）">15570-新项目资深主美（深...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45837" title="18432-微黄金产品运营经理">18432-微黄金产品运营经理</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45831" title="PCG14-二次元类产品运营（深圳）">PCG14-二次元类产品运营...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45817" title="TME-Moo音乐Android开发工程师（深圳）">TME-Moo音乐Android开...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    				<tr>
	    					<td>
	    						<a href="position_detail.php?id=45818" title="TME-Moo音乐iOS开发工程师（深圳）">TME-Moo音乐iOS开发...</a>
	    					</td>
	    					<td align="right"><a href="position.php?lid=2218">深圳</a></td>
	    				</tr>
	    				    			</tbody></table>
    '''

def parse_test():
    htmlElement = etree.HTML(text)
    print(type(htmlElement))
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

def parse_tencent_file():
    htmlElement = etree.parse('tencent.html')
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))

def parse_lagou_file():
    parser = etree.HTMLParser(encoding='utf-8')
    htmlElement = etree.parse('lagou.html',parser=parser)
    print(etree.tostring(htmlElement, encoding='utf-8').decode('utf-8'))


if __name__ == '__main__':
    # parse_test()
    # parse_tencent_file()
    parse_lagou_file()